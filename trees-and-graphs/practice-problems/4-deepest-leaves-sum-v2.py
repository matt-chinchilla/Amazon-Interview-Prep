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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfsMax(node):
            if not node:
                return 0
            
            left = dfsMax(node.left)
            right = dfsMax(node.right)
            maxval = max(left,right) +1
            return maxval
        
        if root.left == None and root.right == None:
            return root.val
        
        counter=0
        maxlen = dfsMax(root)
        queue = deque([root])
        ans = deque([0])               
        breakpoint()
        
        while queue and (counter < maxlen):
            current_length = len(queue)
            counter += 1
            
            for _ in range(current_length):
                node = queue.popleft()
                ans.popleft()
                
                if node.left:
                    queue.append(node.left)
                    ans.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    ans.append(node.right.val)

        return sum(ans)

if __name__ == "__main__":
    sol = Solution()
    root = build_tree_from_list([2])
    print(sol.deepestLeavesSum(root))