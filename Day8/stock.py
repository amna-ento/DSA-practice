prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
buy_day = 0

max_profit = 0
sell_day = 0

for i in range(1, len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
        buy_day = i

    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit
        sell_day = i

print("Best Buy Day:", buy_day + 1)
print("Buy Price:", prices[buy_day])

print("Best Sell Day:", sell_day + 1)
print("Sell Price:", prices[sell_day])

print("Maximum Profit:", max_profit)