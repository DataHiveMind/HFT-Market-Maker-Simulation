from typing import List
from .base_alpha import BaseAlphaSignal
from src.HFT_Engine.utils.math_utils import calculate_order_book_imbalance

class BasicImbalanceSignal(BaseAlphaSignal):
    """
    Generates an alpha signal based on order book imbalance at the top level.
    A positive imbalance (more bids than asks) suggests upward pressure,
    while a negative imbalance suggests downward pressure.
    """

    @property
    def name(self) -> str:
        return "basic_imbalance"

    def generate_signal(self, order_book: dict) -> Union[float, None]:
        """
        Generates an alpha signal based on the order book imbalance.

        Args:
            order_book: A dictionary representing the current state of the order book.
                See BaseAlphaSignal for the expected structure.

        Returns:
            The order book imbalance (bid_quantity - ask_quantity).
        """
        bids = order_book.get('bids', [])
        asks = order_book.get('asks', [])
        return calculate_order_book_imbalance(bids, asks)