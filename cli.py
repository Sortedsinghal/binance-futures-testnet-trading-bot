import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_order

def main():
    parser = argparse.ArgumentParser("Binance Futures Testnet Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    print("\nOrder Summary")
    print("-------------")
    for k, v in vars(args).items():
        print(f"{k}: {v}")

    client = BinanceFuturesClient()
    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price,
        args.stop_price
    )

    print("\nOrder Result")
    print("------------")
    print(f"Order ID: {order.get('orderId')}")
    print(f"Status: {order.get('status')}")
    print(f"Executed Qty: {order.get('executedQty')}")
    print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    print("\n✅ Order placed successfully")

if __name__ == "__main__":
    main()
