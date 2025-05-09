from typing import List, Union
from .base_alpha import BaseAlphaSignal

class StatisticalArbSignal(BaseAlphaSignal):
    """
    Generates an alpha signal based on statistical arbitrage between two assets.
    This is a placeholder and requires a model of the relationship
    between the assets (e.g., cointegration).
    """

    def __init__(self, asset1_symbol: str = "AAPL", asset2_symbol: str = "MSFT"):
        """
        Initializes the statistical arbitrage signal generator.

        Args:
            asset1_symbol: The symbol of the first asset.
            asset2_symbol: The symbol of the second asset.
        """
        self.asset1_symbol = asset1_symbol
        self.asset2_symbol = asset2_symbol
        self.prices1 = []
        self.prices2 = []
        self.timestamps = []

    @property
    def name(self) -> str:
        return "statistical_arb"

    def generate_signal(self, order_book: dict) -> Union[float, None]:
        """
        Generates a statistical arbitrage signal.

        Args:
            order_book:  A dictionary representing the current state of the order book.
            In this case, it needs to contain order book information for both
            asset1 and asset2.  For example:
            {
                'AAPL': {
                    'bids': List[List[float]],
                    'asks': List[List[float]],
                    'timestamp': float
                },
                'MSFT': {
                    'bids': List[List[float]],
                    'asks': List[List[float]],
                    'timestamp': float
                }
            }

        Returns:
            A float representing the alpha signal:
            > 0: Asset1 is relatively overpriced (potential sell Asset1, buy Asset2)
            < 0: Asset1 is relatively underpriced (potential buy Asset1, sell Asset2)
            None: Not enough data or no signal
        """
        order_book_asset1 = order_book.get(self.asset1_symbol)
        order_book_asset2 = order_book.get(self.asset2_symbol)

        if not order_book_asset1 or not order_book_asset2:
            return None

        bids1 = order_book_asset1.get('bids', [])
        asks1 = order_book_asset1.get('asks', [])
        bids2 = order_book_asset2.get('bids', [])
        asks2 = order_book_asset2.get('asks', [])
        timestamp = order_book_asset1.get('timestamp') #using asset1 timestamp

        if not bids1 or not asks1 or not bids2 or not asks2:
            return None

        price1 = (bids1[0][0] + asks1[0][0]) / 2.0
        price2 = (bids2[0][0] + asks2[0][0]) / 2.0
        self.prices1.append(price1)
        self.prices2.append(price2)
        self.timestamps.append(timestamp)

        # 3. Calculate spread or other relationship.
        spread = price1 - price2 # Example

        # 4.  Generate signal based on deviation from the mean or model.
        #    This is where you would use your statistical model
        #    (e.g., Bollinger Bands, cointegration deviation).
        mean_spread = np.mean(np.array(self.prices1) - np.array(self.prices2))
        if len(self.prices1) < 2:
            return None
        return mean_spread - spread # If spread is higher than average, return negative signal
