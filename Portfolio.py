stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 140
}

def calculate_investment():
    portfolio = {}
    total_value = 0

    print(" Enter your stock portfolio (type 'done' to finish):")
    while True:
        stock = input("Stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print(" Stock not found in dictionary. Try again.")
            continue
        qty = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty

    print("\n Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_value += value
        print(f"{stock}: {qty} shares → ${value}")

    print(f"\n Total Investment Value: ${total_value}")

    
    with open("sample_output.csv", "w") as f:
        f.write("Stock,Quantity,Value\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock]*qty}\n")
        f.write(f"TOTAL,,{total_value}\n")

    print("\n Results saved to sample_output.csv")

if __name__ == "__main__":
    calculate_investment()
