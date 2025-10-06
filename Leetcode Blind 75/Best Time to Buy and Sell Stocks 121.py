def maxProfit(prices):
    l = 0  # left pointer at start of list
    r = 1  # right pointer at second position
    max_profit = 0  # current max profit

    while r < len(prices):  # whilst right pointer is in bounds
        if prices[l] < prices[r]:  # if left point is smaller than right  ie there is profit
            profit = prices[r] - prices[l]  # current profit
            max_profit = max(profit, max_profit)  # max_profit = the current profit or max profit depending on whos larger
        else:
            l = r  # moves left pointer to right pointer location as new low prices has been found  previous max_profit has already been recorded anyway so no data loss
        r += 1  # moves right pointer by 1 regardless if profit is found
    return max_profit

print(maxProfit([10,3,5,67,8]))
print(maxProfit([10, 1]))