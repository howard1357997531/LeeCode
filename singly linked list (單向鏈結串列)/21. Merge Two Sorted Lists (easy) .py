from typing import Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

# test
list1_data = [1, 2, 4]; list2_data = [1, 3, 4]
# list1_data = []; list2_data = []
# list1_data = []; list2_data = [0]

list1 = build_singly_linked_list(list1_data)
list2 = build_singly_linked_list(list2_data)
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
result = print_singly_linked_list(merged_list)
print(result)