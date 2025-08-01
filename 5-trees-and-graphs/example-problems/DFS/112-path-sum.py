from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"Val = {self.val}"
    
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False

            ## Check if its a leaf
            if node.left == None and node.right == None:
                return (curr + node.val == targetSum)
            
            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right
        
        return dfs(root, 0)
    
if __name__ == "__main__":
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n1 = TreeNode(1)

    n11 = TreeNode(11, n7, n2)
    n13 = TreeNode(13)
    n4_right = TreeNode(4, None, n1)

    n4_left = TreeNode(4, n11, None)
    n8 = TreeNode(8, n13, n4_right)

    root = TreeNode(5, n4_left, n8)

    sol = Solution()
    print(sol.hasPathSum(root,22)) 