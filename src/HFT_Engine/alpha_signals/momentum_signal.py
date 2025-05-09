# src/hft_engine/alpha_signals/momentum_signal.py
from typing import List, Union
from .base_alpha import BaseAlphaSignal

class MomentumSignal(BaseAlphaSignal):
    """
    Generates an alpha signal based on short-term price momentum.
    This version uses a simple moving average crossover.
    """

    def __init__(self, short_window: int = 5, long_window: int = 20):
        """
        Initializes the momentum signal generator.

        Args:
            short_window: The window for the short-term moving average.
            long_window: The window for the long-term moving average.
        """
        self.short_window = short_window
        self.long_window = long_window
        self.prices = []  # Store recent prices
        self.timestamps = []

    @property
    def name(self) -> str:
        return "momentum"

    def generate_signal(self, order_book: dict) -> Union[float, None]:
        """
        Generates a momentum signal based on recent prices.

        Args:
            order_book: A dictionary representing the current state of the order book.
              We only need the best bid/ask to calculate a price.

        Returns:
            A float representing the alpha signal:
            > 0: Short-term momentum is up (potential buy)
            < 0: Short-term momentum is down (potential sell)
            None: Not enough data
        """
        bids = order_book.get('bids', [])
        asks = order_book.get('asks', [])
        timestamp = order_book.get('timestamp')

        if not bids or not asks:
            return None

        # Use the mid-price as the price
        price = (bids[0][0] + asks[0][0]) / 2.0
        self.prices.append(price)
        self.timestamps.append(timestamp)

        # Keep only the last 'long_window' prices
        if len(self.prices) > self.long_window:
            self.prices = self.prices[-self.long_window:]
            self.timestamps = self.timestamps[-self.long_window:]

        if len(self.prices) < self.long_window:
            return None  # Not enough data yet

        # Calculate moving averages
        short_ma = np.mean(self.prices[-self.short_window:])
        long_ma = np.mean(self.prices)

        return short_ma - long_ma