def validate_side(side):
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ("MARKET", "LIMIT", "STOP_LIMIT"):
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

def validate_price(price, order_type):
    if order_type in ("LIMIT", "STOP_LIMIT") and price is None:
        raise ValueError("Price is required for LIMIT and STOP_LIMIT")
