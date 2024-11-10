from typing import Optional
from tool import TreeNode, build_binary_tree

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # 如果 p q 都是 None
            return True

        if not p or not q:   # 如果 p q 其中一個為 None 表示兩個不同，回傳 false
            return False

        if p.val != q.val:
            return False

        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)

        return left_check and right_check

# test
p = [1,2,3]; q = [1,2,3]
# p = [1,2]; q = [1,None,2]
# p = [1,2,1]; q = [1,1,2]

p_tree = build_binary_tree(p)
q_tree = build_binary_tree(q)

# print(q_tree.val)
# print(q_tree.left.val)
# print(q_tree.right.val)

solution = Solution()
ans = solution.isSameTree(p_tree, q_tree)
print(ans)