# Buy and Sell Stock
prices = [7,1,5,3,6,4]
l,r = 0, 1 #left = buy. right = sell
maxProfit = 0

while r < len(prices):
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxProfit = max(maxProfit, profit)
    else:
         l = r
    r += 1

print(maxProfit)



