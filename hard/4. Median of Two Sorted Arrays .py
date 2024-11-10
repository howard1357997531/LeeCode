from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_list = nums1 + nums2
        num_list.sort()
        num_count = len(num_list)
        first_index = num_count // 2

        if num_count % 2 == 0:
            output = (num_list[first_index -1] + num_list[first_index]) / 2
        else:
            output = float(num_list[first_index])

        return round(output, 5)

nums1 = [1,3]; nums2 = [2]
nums1 = [1,2]; nums2 = [3,4]
nums1 = [1]; nums2 = []

solution = Solution()
ans = solution.findMedianSortedArrays(nums1, nums2)
print(ans)
