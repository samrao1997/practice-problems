# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm
# to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.


def max_profit(prices):
    if len(prices) == 0: return 0

    curr_max_profit = 0
    min_price = prices[0]

    for i in range(len(prices)):
        if (prices[i] < min_price):
            min_price = prices[i]
        elif (prices[i] - min_price > curr_max_profit):
            curr_max_profit = prices[i] - min_price
    return curr_max_profit




print(max_profit([7,1,5,3,6,4]), "  <---- Should be 5")
print(max_profit([7,6,4,3,1]), "  <---- Should be 0")

