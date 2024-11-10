from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
            
        return nums.index(target)


nums = [1,3,5,6]; target = 5
nums = [1,3,5,6]; target = 2
nums = [1,3,5,6]; target = 7

solution = Solution()
ans = solution.searchInsert(nums, target)
print(ans)