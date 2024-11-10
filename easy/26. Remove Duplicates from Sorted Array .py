from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sn = sorted(list(set(nums)))
        nums[:]= sn
        return len(nums)

nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

solution = Solution()
ans = solution.removeDuplicates(nums)
print(ans)