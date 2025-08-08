#Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"Val = {self.val}"        
        
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
    
if __name__ == "__main__":
    s = Solution()
    root1_left = TreeNode(2)
    root1_right = TreeNode(3)
    head1 = TreeNode(1, root1_left, root1_right)
    
    root2_left = TreeNode(3)
    root2_right = TreeNode(2)
    head2 = TreeNode(1, root2_left, root2_right)
    
    print(s.leafSimilar(head1, head2))