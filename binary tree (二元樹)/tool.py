# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_binary_tree(data):
    if not data:
        return None

    root = TreeNode(data[0])
    i = 1
    queue = [root]

    while queue:
        node = queue.pop(0)
        if i < len(data) and data[i]:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1
        if i < len(data) and data[i]:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1

    return root