from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"Val = {self.val}"
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        breakpoint()
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) +1                  # left & right == 0 means it is a LEAF & increments a counter
        breakpoint()
        
if __name__ == "__main__":
    sol = Solution()
    
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    
    n9 = TreeNode(9)
    n20 = TreeNode(20, n15, n7)
    
    root = TreeNode(3, n9, n20)
    
    sol.maxDepth(root)