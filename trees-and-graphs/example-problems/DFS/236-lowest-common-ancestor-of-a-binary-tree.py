from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__ (self):
        return f"TreeNode == ({self.val})"
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case  // empty
        breakpoint()
        if not root:
            return None
        
        # p or q are the root
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)#type: ignore
        right = self.lowestCommonAncestor(root.right, p, q)#type: ignore
        
        # p and q are in diff subtrees of the root, therefore the answer is the root
        if left and right:
            return root
        
        # p and q are actually in a subtree! great success!
        if left:
            return left
        
        return right
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    root.left = n5
    root.right = n1

    n5.left = n6
    n5.right = n2

    n1.left = n0
    n1.right = n8

    n2.left = n7
    n2.right = n4
    
    lac = sol.lowestCommonAncestor(root, n6, n4)
    print(lac)