from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__ (self):
        return f"TreeNode == ({self.val})"
    
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        breakpoint()

        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left) #type:ignore
        right = self.isSameTree(p.right, q.right)#type:ignore
        
        return left and right
    
if __name__ == "__main__":
    sol = Solution()
    
    p_left = TreeNode(2)
    p_right = TreeNode(3)
    p = TreeNode(1, p_left, p_right)
    
    # Second tree (right in the image)
    q_left = TreeNode(2)
    q_right = TreeNode(3)
    q = TreeNode(1, q_left, q_right)
    
    # Example call
    print(sol.isSameTree(p, q))