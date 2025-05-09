import numpy as np
from typing import List, Union

def calculate_vwap(prices: List[float], volumes: List[float]) -> Union[float, None]:
    """
    Calculates the Volume Weighted Average Price (VWAP).

    Args:
        prices: A list of prices.
        volumes: A list of volumes corresponding to the prices.

    Returns:
        The VWAP as a float, or None if the input lists are invalid.
    """
    if not prices or not volumes or len(prices) != len(volumes):
        return None  # Handle invalid input

    prices = np.array(prices)
    volumes = np.array(volumes)
    return np.sum(prices * volumes) / np.sum(volumes)

def calculate_order_book_imbalance(bids: List[List[float]], asks: List[List[float]]) -> float:
    """
    Calculates a simple order book imbalance.

    This version calculates the imbalance as the difference between the total
    bid quantity and the total ask quantity at the top level.

    Args:
        bids: A list of bid orders, where each bid is [price, quantity].
        asks: A list of ask orders, where each ask is [price, quantity].

    Returns:
        The order book imbalance (bid_quantity - ask_quantity).
    """
    if not bids or not asks:
        return 0.0  # Handle empty order book sides

    total_bid_quantity = sum(bid[1] for bid in bids)
    total_ask_quantity = sum(ask[1] for ask in asks)
    return total_bid_quantity - total_ask_quantity

def calculate_mid_price(best_bid: float, best_ask: float) -> float:
    """
    Calculates the mid-price given the best bid and ask.

    Args:
        best_bid: The best bid price.
        best_ask: The best ask price.

    Returns:
        The mid-price.
    """
    return (best_bid + best_ask) / 2.0
