import yfinance as yf
from tabulate import tabulate

portfolio = {}

def add_stock(symbol, quantity, buy_price):
    symbol = symbol.upper()
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
        # update average buy price
        total_cost = (portfolio[symbol]['avg_buy_price'] * portfolio[symbol]['quantity']) + (buy_price * quantity)
        total_qty = portfolio[symbol]['quantity']
        portfolio[symbol]['avg_buy_price'] = total_cost / total_qty
    else:
        portfolio[symbol] = {
            'quantity': quantity,
            'avg_buy_price': buy_price
        }

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
    else:
        print("Stock not found in portfolio.")

def get_live_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.history(period='1d')['Close'].iloc[-1]
        return round(price, 2)
    except:
        return None

def view_portfolio():
    table = []
    total_value = 0
    total_cost = 0
    for symbol, data in portfolio.items():
        live_price = get_live_price(symbol)
        if live_price is None:
            continue
        qty = data['quantity']
        buy_price = data['avg_buy_price']
        value = round(live_price * qty, 2)
        cost = round(buy_price * qty, 2)
        gain = round(value - cost, 2)
        gain_pct = round((gain / cost) * 100, 2) if cost else 0
        total_value += value
        total_cost += cost
        table.append([symbol, qty, buy_price, live_price, value, gain, f"{gain_pct}%"])
    
    print(tabulate(table, headers=["Symbol", "Qty", "Buy Price", "Live Price", "Value", "Gain", "Gain %"], tablefmt="fancy_grid"))
    print(f"\nTotal Portfolio Value: ₹{round(total_value,2)}")
    print(f"Total Investment Cost: ₹{round(total_cost,2)}")
    print(f"Net Gain/Loss: ₹{round(total_value - total_cost, 2)}")

def main():
    print("📊 Welcome to the Stock Portfolio Tracker")
    while True:
        print("\nOptions: add / remove / view / quit")
        cmd = input("Enter command: ").strip().lower()
        if cmd == 'add':
            symbol = input("Stock Symbol: ").strip()
            qty = int(input("Quantity: "))
            price = float(input("Buy Price per share: "))
            add_stock(symbol, qty, price)
        elif cmd == 'remove':
            symbol = input("Stock Symbol to remove: ").strip()
            remove_stock(symbol)
        elif cmd == 'view':
            view_portfolio()
        elif cmd == 'quit':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
