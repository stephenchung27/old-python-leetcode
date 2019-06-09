'''
Buy and Sell a Stock at Most k Times

Write a program to compute the maximum profit that can be made by buying and selling a share at most k times over a given day range. 
Your program takes k and an array of daily stock prices as input.

Example:
Input: [225, 220, 230, 245, 235, 230, 250, 260, 210, 200, 245, 255, 240]
Output: (245 - 220) + (260 - 230) + (255 - 200) = 110

Find extrema in monotonic order
Get differences
'''
import heapq
def buy_and_sell_stock_k_times(prices, k):
    if k == 0:
        return 0.0
    elif 2 * k >= len(prices):
        return sum(max(0, b - a) for a, b in zip(prices[:-1], prices[1:]))
    min_prices, max_profits = [float('inf')] * k, [0.0] * k
    for price in prices:
        print(price)
        for i in reversed(range(k)):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i], price - (0 if i == 0 else max_profits[i - 1]))
            print(max_profits)
            print(min_prices)
    return max_profits[-1]

print(buy_and_sell_stock_k_times(
    [225, 220, 230, 245, 235, 230, 250, 260, 210, 200, 245, 255, 240], 2))
