from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        target = str(int(''.join(map(str, digits))) + 1)
        output = [int(i) for i in target]
        return output


digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]

solution = Solution()
ans = solution.plusOne(digits)
print(ans)