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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        breakpoint()
        closest = root.val#type:ignore
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target- x), x)) 
            root = root.left if target < root.val else root.right
        return closest

if __name__ == "__main__":
    sol = Solution()
    root = build_tree_from_list([4,2,7,1,3])
    print(sol.closestValue(root, 3.714286))