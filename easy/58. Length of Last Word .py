class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = s.strip().split()[-1]
        return len(output)


s = "Hello World"
s = "   fly me   to   the moon  "
s = "luffy is still joyboy"

solution = Solution()
ans = solution.lengthOfLastWord(s)
print(ans)