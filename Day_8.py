# Buy and Sell Stock
prices = [7,1,5,3,6,4]
max_price = max(prices)
min_price = min(prices)
buy_price = 0
sell_price = 0
max_profit = 0
if prices == sorted(prices, reverse=True):   
    print(max_profit)
else:
    i = 0
    while i < len(prices):
        if prices[i] ==  min_price:
            buy_price = prices[i]
        i = i + 1
        
    j = 1
    while j < len(prices):
        if prices[j] ==  max_price:
            sell_price = prices[j]
        j = j + 1
        
    print(buy_price)
    print(sell_price)
    max_profit = sell_price - buy_price
    print(max_profit)


