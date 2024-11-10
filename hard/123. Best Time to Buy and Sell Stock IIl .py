from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # float('inf')：代表正無窮大，這個值比任何有限的數字都大。
        # float('-inf')：代表負無窮大，這個值比任何有限的數字都小。
        # initialize variables for first buy, first sell, second buy, and second sell
        buy1, buy2 = float('inf'), float('inf')
        sell1, sell2 = 0, 0

        # iterate over prices to update buy and sell values
        for price in prices:
            # update first buy and sell values
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            # update second buy and sell values
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
            print(buy1, sell1, buy2, sell2)

        return sell2

prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [1,2,4,2,5,7,2,4,9,0]

solution = Solution()
ans = solution.maxProfit(prices)
print(ans)

'''
The basic idea is to iterate over the array of stock prices and update four variables:

buy1 - the minimum price seen so far for the first transaction
sell1 - the maximum profit seen so far for the first transaction
buy2 - the minimum price seen so far for the second transaction, taking into account the profit from the first transaction
sell2 - the maximum profit seen so far for the second transaction
At the end of the iteration, the value of sell2 is returned as the maximum profit achievable with two transactions.

The if not prices check is included to handle the edge case where the input array is empty.

Here's how the algorithm works step by step for the input [3,3,5,0,0,3,1,4]:

1. Initialize buy1, buy2, sell1, and sell2 to inf, inf, 0, and 0, respectively.
2. For the first price of 3, update buy1 to 3, sell1 to 0, buy2 to -3, and sell2 to 0.
3. For the second price of 3, update buy1 to 3, sell1 to 0, buy2 to -3, and sell2 to 0 (no change).
4. For the third price of 5, update buy1 to 3, sell1 to 2, buy2 to -1, and sell2 to 2.
5. For the fourth price of 0, update buy1 to 0, sell1 to 2, buy2 to -1, and sell2 to 2 (no change).
6. For the fifth price of 0, update buy1 to 0, sell1 to 2, buy2 to -2, and sell2 to 2 (no change).
7. For the sixth price of 3, update buy1 to 0, sell1 to 3, buy2 to 0, and sell2 to 3.
8. For the seventh price of 1, update buy1 to 0, sell1 to 3, buy2 to -3, and sell2 to 3 (no change).
9. For the eighth price of 4, update buy1 to 0, sell1 to 4, buy2 to 0, and sell2 to 4
'''