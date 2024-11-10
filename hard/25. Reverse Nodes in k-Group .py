from typing import List, Optional
from ..tool import build_singly_linked_list, print_singly_linked_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

head = [1,2,3,4,5]; k = 2
head = [1,2,3,4,5]; k = 3

lists_data = build_singly_linked_list(head)
solution = Solution()
merged_list = solution.reverseKGroup(lists_data)
answer = print_singly_linked_list(merged_list)
print(answer)