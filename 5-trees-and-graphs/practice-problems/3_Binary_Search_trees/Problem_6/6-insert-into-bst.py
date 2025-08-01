from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"Val = {self.val}"
    
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])#type:ignore
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])#type:ignore
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:    
        def dfs(node):
            if not node:
                return None
            
            if (val < node.val and not node.left) or (val > node.val and not node.right):
                return node
            
            if val < node.val:
                return dfs(node.left)
            elif val > node.val:
                return dfs(node.right)
            else:
                return node
    #-----------------------------------------------------------------
        if not root:
            return TreeNode(val)
        
        target = dfs(root)
        newNode = TreeNode(val)
        
        if newNode.val < target.val:#type:ignore
            target.left = newNode#type:ignore
        else:
            target.right = newNode#type:ignore
        
        return root

if __name__ == "__main__":
    sol = Solution()
    root = build_tree_from_list([4,2,7,1,3])
    print(sol.insertIntoBST(root, 5))