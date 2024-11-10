class Solution:
    def mySqrt(self, x: int) -> int:
        output = x ** 0.5
        return int(output)


x = 4
# x = 8

solution = Solution()
ans = solution.mySqrt(x)
print(ans)