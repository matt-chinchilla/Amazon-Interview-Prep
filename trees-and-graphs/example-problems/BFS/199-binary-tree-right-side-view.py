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
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return []
        breakpoint()
        queue = deque([root])
        ans = []
        
        while queue:

            current_length = len(queue)
            ans.append(queue[-1].val)           # Append the rightmost element
             
            for _ in range(current_length):     # Once I have traversed the current level of the tree
                node = queue.popleft()          # Remove the elements of the previous level
                if node.left:
                    queue.append(node.left)     # Add a left child if there is one
                if node.right:  
                    queue.append(node.right)    # Add a right child if there is one

        return ans
    
if __name__ == "__main__":
    sol = Solution()
    root = build_tree_from_list([1,2,3,None,5,None,4])
    print(sol.rightSideView(root))