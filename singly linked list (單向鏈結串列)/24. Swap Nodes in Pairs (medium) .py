from typing import Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head

        # 如果為 [] 或只有一個數 [1]
        if not head or not head.next:
            return p
        
        odd = True
        while head:
            if head.next:
                if odd:
                    head.val, head.next.val = head.next.val, head.val
                    odd = False
                else:
                    odd = True
                head = head.next
            else:
                head = head.next

        return p
        
# test
head_data = [1,2,3,4]    # [2, 1, 4, 3]
head_data = []           # []
head_data = [1]          # [1]
# head_data = [1,2,3]    # [2, 1, 3]

head = build_singly_linked_list(head_data)
solution = Solution()
new_head = solution.swapPairs(head)
result = print_singly_linked_list(new_head)
print(result)