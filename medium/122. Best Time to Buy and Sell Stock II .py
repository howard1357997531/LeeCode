from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 先暫存第1個值為 temp_num，後面的值會變成下個 temp_num，
        # 若下個值比 temp_num 大，相減後加進 profit 做累積比較，比 profit 大就存到 profit
        temp_num = prices[0]
        profit = 0

        for i in range(len(prices)):
            if i+1 == len(prices): break # 不計算最後一個

            next_num = prices[i+1]

            # 順便也檢查 prices 是不是降冪(前一個一定比下一個大)，是 profit 的話不變 = 0
            if temp_num >= next_num:
                temp_num = next_num
            else:
                price = next_num - temp_num
                profit += price
                temp_num = next_num
            
        return profit

prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

solution = Solution()
ans = solution.maxProfit(prices)
print(ans)