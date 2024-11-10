from typing import List, Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        duplicate_num = float("-inf")

        while head:
            if head.next and (head.val == head.next.val or head.val == duplicate_num):
                duplicate_num = head.val
            elif not head.next and head.val == duplicate_num:
                pass
            else:
                # 如果用這樣，最後一個是重複數也會加進去，因為若重複不會跑這邊，所以不會被消除掉
                # result.next = head 
                result.next = ListNode(head.val)
                result = result.next
            head = head.next
        
        return dummy.next


# test
head = [1,2,3,3,4,4,5]  # [1,2,5]
head = [1,1,1,2,3]      # [2,3] 
head = [1,1]            # []
head = [1,2,2]          # [1]

lists_data = build_singly_linked_list(head)
solution = Solution()
merged_list = solution.deleteDuplicates(lists_data)
answer = print_singly_linked_list(merged_list)
print(answer)