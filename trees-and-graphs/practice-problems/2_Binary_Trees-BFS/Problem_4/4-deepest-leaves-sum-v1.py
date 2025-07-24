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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = []               
        len_to_add = []
        final = 0
        
        while queue:
            current_length = len(queue)
            len_to_add.append(current_length)
            
            for _ in range(current_length):
                node = queue.popleft()
                ans.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        for i in range(1, len_to_add[-1]+1):
            final += ans[-i]
            
        return final
    
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_from_list([1,2,3,4,5,None,6,7,None,None,None,None,8])
    sol.deepestLeavesSum(root)