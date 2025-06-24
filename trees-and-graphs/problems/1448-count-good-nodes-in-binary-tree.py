from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__ (self):
        return f"TreeNode == ({self.val})"
    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_so_far: int):
            if not node:
                return 0
            
            left = dfs(node.left, max(max_so_far, node.val))
            right = dfs(node.right, max(max_so_far, node.val))
            ans = left + right
            
            if node.val >= max_so_far:
                ans += 1
                
            return ans
        
        return dfs(root, float("-inf"))#type:ignore             # neg infinity b/c there are no nodes that come before the root
    
if __name__ == "__main__":
    sol = Solution()
    
    n3_left = TreeNode(3)
    n1_right = TreeNode(1)
    n5 = TreeNode(5)

    n1_left = TreeNode(1, n3_left, None)         # left child = 3, right = None
    n4 = TreeNode(4, n1_right, n5)               # left child = 1, right = 5

    root = TreeNode(3, n1_left, n4)              # left child = n1_left, right = n4
    
    sol.goodNodes(root)