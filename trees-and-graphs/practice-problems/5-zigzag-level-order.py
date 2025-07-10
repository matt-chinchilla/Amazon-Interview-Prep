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
    def zigzagLevelOrder(self, root: Optional['TreeNode']):
        if not root:
            return []
        
        next_level = deque([root,])
        nl_vals = [root.val]
        ans = []
        every_other = 2
        
        while next_level:
            if every_other % 2 == 0:
                ans += [list(nl_vals)]                
            elif every_other % 2 == 1:
                ans += [list(nl_vals[::-1])]
            
            curr_level = next_level
            next_level, nl_vals = deque(), []
            every_other += 1
            
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                    nl_vals.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    nl_vals.append(node.right.val)
        
        return ans