class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
    
        num_list = [int(i) for i in str(x)]
        num_list_reverse = list(reversed(num_list))
        return num_list == num_list_reverse
    
x = 121
x = -121
x = 10

solution = Solution()
ans = solution.isPalindrome(x)
print(ans)