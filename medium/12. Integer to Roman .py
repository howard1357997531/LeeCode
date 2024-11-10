class Solution:
    def intToRoman(self, num: int) -> str:
        pass

# test
num = 3749  # "MMMDCCXLIX"
num = 58    # "LVIII"
num = 1994  # "MCMXCIV"

solution = Solution()
ans = solution.intToRoman(num)
print(ans)