from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__ (self):
        return f"TreeNode == ({self.val})"

from collections import deque
    
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, max_value, min_value):
            breakpoint()
            if root is None:
                return max_value - min_value
             
            max_value = max(max_value, root.val)
            min_value = min(min_value, root.val)
            
            left = dfs(root.left, max_value, min_value)
            right = dfs(root.right, max_value, min_value)
  
            return max(right, left)
        
        return dfs(root, root.val, root.val)#type:ignore

    
if __name__ == "__main__":
    sol = Solution()
    
    n8  = TreeNode(8)
    n3  = TreeNode(3)
    n10 = TreeNode(10)
    n1  = TreeNode(1)
    n6  = TreeNode(6)
    n14 = TreeNode(14)
    n4  = TreeNode(4)
    n7  = TreeNode(7)
    n13 = TreeNode(13)


    n8.left  = n3
    n8.right = n10

    n3.left  = n1
    n3.right = n6

    n6.left  = n4
    n6.right = n7

    n10.right = n14

    n14.left  = n13

    sol.maxAncestorDiff(n8)
    # def dfs(node):