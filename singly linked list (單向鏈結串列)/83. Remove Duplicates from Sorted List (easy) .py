from typing import Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head # 直接修改

        while head:
            if head.next and head.val == head.next.val:
                if head.next.next:
                    # head 的 val 不變，head.next 變下下個
                    head.next = head.next.next
                else:
                    # 若來到(倒數第2個)，會沒有下下個(head.next.next)
                    head.next = None
            else:
                head = head.next
        return p

# test
head_data = [1, 1, 2, 3, 3]

head = build_singly_linked_list(head_data)
solution = Solution()
new_head = solution.deleteDuplicates(head)
result = print_singly_linked_list(new_head)
print(result)