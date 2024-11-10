from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = len(nums)
        for i in range(count):
            first = nums[i]
            for j in range(count-i-1):
                second = nums[i+j+1]
                if first + second == target:
                    return [i, i+j+1]
                
nums = [2,7,11,15]; target = 9
nums = [3,2,4]; target = 6
nums = [3,3]; target = 6

solution = Solution()
ans = solution.twoSum(nums, target)
print(ans)