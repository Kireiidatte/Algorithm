import sys

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price-min_price)

    return profit