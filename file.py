# Stock Portfolio Tracker

# Dictionary to store stock prices
stock_prices = {
    "AAPL": 150,
    "GOOGL": 2500,
    "MSFT": 200
}

def get_user_portfolio():
    # Input/Output: Get user input for stock names and quantities
    #portfolio = {}
    #while True:
        stock_name = input("Enter stock name (or 'done' to finish): ")
        #if stock_name.lower() == 'done':
            #break
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        #portfolio[stock_name] = quantity
    #return portfolio

def calculate_portfolio_value(portfolio):
    # Basic arithmetic: Calculate total portfolio value
    total_value = 0
    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            total_value += stock_prices[stock] * quantity
        else:
            print(f"Price not found for {stock}")
    return total_value

def save_portfolio(portfolio, total_value):
    # File handling: Save portfolio to a file
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio:\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity}\n")
        file.write(f"Total Value: {total_value}\n")

def main():
    portfolio = get_user_portfolio()
    total_value = calculate_portfolio_value(portfolio)
    print(f"Total Portfolio Value: {total_value}")
    save_portfolio(portfolio, total_value)
    print("Portfolio saved to portfolio.txt")

if __name__ == "__main__":
    main()