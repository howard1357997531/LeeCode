class Solution:
    def climbStairs(self, n: int) -> int:
        output = [0, 1, 2]

        if n > 2:
            for i in range(3, n+1):
                output.append(output[i-1] + output[i-2])

        return output[n]

n = 1  # 1
n = 2  # 2
n = 3  # 3
n = 4  # 5
n = 5  # 8
n = 1  # 13

solution = Solution()
ans = solution.climbStairs(n)
print(ans)