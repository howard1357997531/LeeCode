from typing import List, Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

# test
lists = [[1,4,5],[1,3,4],[2,6]]  # [1,1,2,3,4,4,5,6]
lists = []                       # []
lists = [[]]                     # []

lists_data = build_singly_linked_list(lists)
solution = Solution()
merged_list = solution.mergeKLists(lists_data)
answer = print_singly_linked_list(merged_list)
print(answer)