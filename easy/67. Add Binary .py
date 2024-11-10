class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        output = a + b
        return bin(output)[2:]


a = "11"; b = "1"
a = "1010"; b = "1011"

solution = Solution()
ans = solution.addBinary(a, b)
print(ans)