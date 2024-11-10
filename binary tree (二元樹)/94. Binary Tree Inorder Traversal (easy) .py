from typing import List, Optional
from tool import TreeNode, build_binary_tree

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # 定義一個遞歸函數
        def inorder(node):
            if node:
                # 先遍歷左子樹
                inorder(node.left)
                # 然後訪問當前節點
                result.append(node.val)
                # 最後遍歷右子樹
                inorder(node.right)
        
        inorder(root)  # 開始從根節點進行中序遍歷
        return result

# test
root = [1,None,2,3]
root = [1,2,3,4,5,None,8,None,None,6,7,9]
# root = []

tree = build_binary_tree(root)
print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.left.left.val)
print(tree.left.right.val)
print(root)
solution = Solution()
ans = solution.inorderTraversal(tree)
print(ans)