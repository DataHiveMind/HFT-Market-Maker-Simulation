from abc import ABC, abstractmethod
from typing import List, Union

class BaseAlphaSignal(ABC):
    """
    Abstract base class for alpha signal generation.  All alpha signal
    classes should inherit from this class.
    """

    @abstractmethod
    def generate_signal(self, order_book: dict) -> Union[float, None]:
        """
        Generates an alpha signal based on the current order book.

        Args:
            order_book: A dictionary representing the current state of the order book.
                The structure of the order_book dict is assumed to be:
                {
                    'bids': List[List[float]],  # [[price, quantity], ...]
                    'asks': List[List[float]],  # [[price, quantity], ...]
                    'timestamp': float
                }

        Returns:
            A float representing the alpha signal.  None indicates no signal.
            The interpretation of the signal (buy/sell) is up to the
            execution logic.  For example:
                - Positive signal:  Indicates upward price pressure, potential buy.
                - Negative signal: Indicates downward price pressure, potential sell.
                - 0 or None:  Neutral.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the alpha signal.  This is used for logging
        and identification.
        """
        pass