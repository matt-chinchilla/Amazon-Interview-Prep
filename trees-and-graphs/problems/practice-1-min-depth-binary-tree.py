import queue
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__ (self):
        return f"TreeNode == ({self.val})"
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return 0
            
            # If only one of child is non-null, then go into that recursion.
            if root.left is None:
                return 1 + dfs(root.right)
            
            elif root.right is None:
                return 1 + dfs(root.left)
            
            # Both children are non-null, hence call for both children.
            return 1 + min(dfs(root.left), dfs(root.right))

        return dfs(root)
                
if __name__ == "__main__":
    sol = Solution()
    
    root = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    
    root.right = n3
    n3.right = n4
    n4.right = n5
    n5.right = n6
    
    min_depth = sol.minDepth(root)
    print(min_depth)