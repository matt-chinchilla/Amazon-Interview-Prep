from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__ (self):
        return f"TreeNode == ({self.val})"
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        self.max_diameter = 0
            
        def dfs(node) -> int:
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
    
            current_diameter = left + right
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            return max(left, right) +1
        
        dfs(root)
        return self.max_diameter
    
if __name__ == "__main__":
    sol = Solution()
    
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    root.left = n2
    root.right = n3

    n2.left = n4
    n2.right = n5
    
    print(sol.diameterOfBinaryTree(root))