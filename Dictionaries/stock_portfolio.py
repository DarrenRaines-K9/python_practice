ticker_symbols = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

# create a list of purchases (ticket symbol, shares purchased, date of purchase, share price)
purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

# create a dictionary with ticker symbol as key and list of purchases as value
purchases2 = {
    'GE': [('GE', 100, '10-sep-2001', 48), ('GE', 200, '1-jul-1998', 56)],
    'CAT': [('CAT', 100, '1-apr-1999', 24)],
    'GM': [('GM', 50, '15-aug-2000', 35)],
    'AAPL': [('AAPL', 150, '20-dec-2005', 120), ('AAPL', 100, '15-jan-2007', 130)],
    'NVDA': [('NVDA', 200, '10-oct-2010', 20), ('NVDA', 100, '5-may-2012', 30)]
}


def purchase_prices(purchases, ticker_symbols):
    total_cost = 0
    for purchase in purchases:
        ticker_symbol, shares, date, price = purchase
        company_name = ticker_symbols.get(ticker_symbol, "Unknown Company")
        cost = shares * price
        total_cost += cost
        print(f"Purchased {shares} shares of {company_name} ({ticker_symbol}) on {date} at ${price} per share. Total cost: ${cost}")
    print(f"Total cost of all purchases: ${total_cost}")

# get total cost of purchases and print details
purchase_prices(purchases, ticker_symbols)

# total investment by ticker symbol
def total_investment_by_ticker(purchases_dict):
    investment = {}

    for ticker, purchase_list in purchases_dict.items():
        total = 0
        for _, shares, date, price in purchase_list:
            total += shares * price
        investment[ticker] = total

    return investment

def print_investment_by_ticker(investment, ticker_symbols):
    for ticker_symbol, total_cost in investment.items():
        company_name = ticker_symbols.get(ticker_symbol, "Unknown Company")
        print(f"Total investment in {company_name} ({ticker_symbol}): ${total_cost}")   

print("\nTotal investment by ticker symbol:")
investment = total_investment_by_ticker(purchases2)
print_investment_by_ticker(investment, ticker_symbols)