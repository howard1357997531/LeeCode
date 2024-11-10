class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            output = int(str(x)[1:][::-1]) * -1
        else:
            output = int(str(x)[::-1])

        # 這樣寫比較吃效能
        # if not (2**31)*-1 <= output <= 2**31 - 1:
        #     return 0
        
        if output > 2**31 - 1 or (2**31)*-1 > output:
            return 0
        
        return output

x = 123
x = -123
# x = 120
# x = 1534236469

solution = Solution()
ans = solution.reverse(x)
print(ans)
print(2 * -1)