from binance.enums import *
from .validators import *
from .logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    validate_price(price, order_type)

    try:
        logger.info(f"Request: {symbol} {side} {order_type} qty={quantity}")

        if order_type == "MARKET":
            order = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )

        elif order_type == "STOP_LIMIT":
            order = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC
            )


        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error: {e}")
        raise
