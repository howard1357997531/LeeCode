from typing import Optional
from tool import ListNode, build_singly_linked_list, print_singly_linked_list

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        head_count = 0
        head_count_node = head

        while head_count_node:
            head_count_node = head_count_node.next
            head_count += 1

        seperate_count = 0  # 區分左右邊位置

        if head_count - k == 0:
            return head
        elif head_count - k > 0:
            seperate_count = head_count - k
        else:
            seperate_count = head_count - (k % head_count)

        # 先把左邊部分存起來
        left_node = ListNode(0, head)
        left_result = left_node

        for _ in range(seperate_count):
            left_result = left_result.next
            head = head.next
        left_result.next = None

        # 把右邊部分變成起始
        right_node = ListNode(0, head)
        right_result = right_node

        while head:
            right_result = right_result.next
            head = head.next
        
        # 右邊尾部加上左邊
        right_result.next = left_node.next

        return right_node.next

# test
head = [1,2,3,4,5]; k = 2  # [4,5,1,2,3]
# head = [0,1,2]; k = 4      # [2,0,1]
# head = []; k = 1           # [2,0,1]

lists_data = build_singly_linked_list(head)
solution = Solution()
merged_list = solution.rotateRight(lists_data, k)
answer = print_singly_linked_list(merged_list)
print(answer)