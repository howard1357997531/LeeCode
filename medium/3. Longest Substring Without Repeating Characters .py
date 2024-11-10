class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right-left+1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        print(charSet)
        return maxLength

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"

solution = Solution()
ans = solution.lengthOfLongestSubstring(s)
print(ans)