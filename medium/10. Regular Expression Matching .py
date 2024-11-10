import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 可以將正則表達式動態生成，而不是直接使用靜態的 r'' 字符串，
        # 所以可以直接把 p 當作正則表達式的模式
        pattern = p + "$"
        match_obj = re.match(pattern, s)

        return True if match_obj else False

s = "aa"; p = "a"      # False
s = "aa"; p = "a*"     # True
s = "ab"; p = ".*"     # True

solution = Solution()
ans = solution.isMatch(s, p)
print(ans)