from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 先暫存第1個值為 low_num，若後面的值有比 low_num 小，low_num 值變成那個數，
        # 若下個比前個大，相減後跟 profit 比較，比 profit 大就存到 profit
        low_num = prices[0]
        profit = 0

        for i in range(len(prices)):
            if i+1 == len(prices): break # 不計算最後一個

            next_num = prices[i+1]

            # 順便也檢查 prices 是不是降冪(前一個一定比下一個大)，是 profit 的話不變 = 0
            if low_num >= next_num:
                low_num = next_num
            else:
                price = next_num - low_num
                if price > profit:
                    profit = price
            
        return profit

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
# prices = [2,4,1]

solution = Solution()
ans = solution.maxProfit(prices)
print(ans)