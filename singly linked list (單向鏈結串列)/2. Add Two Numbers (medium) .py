from typing import Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        total = 0

        # total > 0 有可能到最後 l1, l2都是None 但 total=1 還需要再加一次
        # ex: l1_data = [2,4,9]; l2_data = [5,6]
        while l1 or l2 or total > 0:
            if l1 :
                total += l1.val
                l1 = l1.next
            if l2 :
                total += l2.val
                l2 = l2.next

            cur.next = ListNode(total % 10) #取整數
            cur = cur.next
            total = total // 10

        return dummy.next

# test
l1_data = [2,4,3]; l2_data = [5,6,4]
l1_data = [0]; l2_data = [0]
l1_data = [2,4,3]; l2_data = [5,6]
l1_data = [2,4,9]; l2_data = [5,6]
l1_data = [9,9,9,9,9,9,9]; l2_data = [9,9,9,9]

l1 = build_singly_linked_list(l1_data)
l2 = build_singly_linked_list(l2_data)
solution = Solution()
merged_list = solution.addTwoNumbers(l1, l2)
result = print_singly_linked_list(merged_list)
print(result)
