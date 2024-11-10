class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = haystack.index(needle) if needle in haystack else -1
        return output


haystack = "sadbutsad"; needle = "sad"
# haystack = "leetcode"; needle = "leeto"

solution = Solution()
ans = solution.strStr(haystack, needle)
print(ans)