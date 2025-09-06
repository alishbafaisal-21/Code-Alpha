                    ####STOCK PORTFOLIO TRACKER####

stock_pr = {"orange" : 120, "apple" : 90, "banana" : 100}

def get_input_portfolio():
    portfolio={}
    while True:
        stock_names = input("Enter the stock name: ")
        if stock_names == "done":
           print("Stocks has finished")
           break
        stock_quantity = int(input("Enter the quantity of {stock_names}:"))
        portfolio[stock_names]=stock_quantity
    return portfolio

def cal_total_investment(portfolio):
    total_investment=0
    for stock_names, stock_quantity in portfolio.items():
        if stock_names in stock_pr:
           total_investment += stock_pr[stock_names] * stock_quantity
        else:
            print("price not found for ", {stock_names})
    return total_investment

def save_data(portfolio, total_investment):
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio:\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity}\n")
        file.write(f"Total Value: {total_investment}\n")

def main():
    portfolio = get_input_portfolio()
    total_investment = cal_total_investment(portfolio)
    print(f"Total Portfolio Value: {total_investment}")
    save_data(portfolio, total_investment)
    print("Portfolio saved to portfolio.txt")

if __name__=="__main__":
    main()



