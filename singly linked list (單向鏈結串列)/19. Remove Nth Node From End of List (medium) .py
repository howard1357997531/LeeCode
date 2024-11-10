from typing import Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        result = dummy

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            result = result.next
        
        result.next = result.next.next

        return dummy.next

# test
head_data = [1,2,3,4,5]; n = 2   # [1,2,3,5]
head_data = [1]; n = 1           # []
# head_data = [1,2]; n = 1         # [1]
head_data = [1,2]; n = 2         # [2]

head = build_singly_linked_list(head_data)
solution = Solution()
new_head = solution.removeNthFromEnd(head, n)
result = print_singly_linked_list(new_head)
print(result)

'''
        if not head: return None
        
        get_head_len = head
        head_len = 0  # head有幾個

        while get_head_len:
            get_head_len = get_head_len.next
            head_len += 1

        if head_len == 1 and n >= 1: return None

        p = head
        p_index = head_len - n
        count = 1

        while head:
            if count == p_index:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
            
            if p_index == 0: # 換第一個
                head.val = head.next.val
                if not head.next.next:
                    head.next = None

            head = head.next
            count += 1

        return p
'''

