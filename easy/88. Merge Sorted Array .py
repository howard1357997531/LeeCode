from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            for _ in range(n):
                nums1.pop()

        nums1.extend(nums2)
        nums1.sort()
        print(nums1)

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
nums1 = [1]; m = 1; nums2 = []; n = 0
nums1 = [0]; m = 0; nums2 = [1]; n = 1
nums1 = [-1,0,0,3,3,3,0,0,0]; m = 6; nums2 = [1,2,2]; n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n) 