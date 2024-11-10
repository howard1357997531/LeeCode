import re

class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r'[-+]?\d+'
        match_obj = re.match(pattern, s.strip())
        
        if match_obj:
            num = int(match_obj.group())

            if num > 2**31 - 1:
                return 2**31 -1
            elif num < 2**31*-1:
                return 2**31*-1
            else:
                return num
        else:
            return 0

s = "42"              # 42
s = " -042"           # -42
s = "1337c0d3"        # 1337
# s = "0-1"             # 0
# s = "words and 987"   # 0
# s = "-91283472332"    # 2**31*-1
# s = "+1"              # 1

solution = Solution()
ans = solution.myAtoi(s)
print(ans)
