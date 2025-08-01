from util import ListNode, Optional
import pdb

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        curr, prev = head, None                                             # Eventually becomes the head for the reversed List
        
        # Move the pointers until they are where they need to be
        while left > 1:
            prev = curr
            curr = curr.next#type: ignore
            left, right = left-1, right-1
        
        # Make the two pointers to bridge the final connections
        tail, connection_node = curr, prev
        
        # Iterative reverse nodes until left becomes 0
        while right:
            third = curr.next #type: ignore
            curr.next = prev #type: ignore
            prev = curr
            curr = third
            right -= 1
            
        if connection_node:
            connection_node.next = prev
        else:
            head = prev
            
        tail.next = curr#type: ignore
        
        return head

if __name__ == "__main__":
    node1 = ListNode(1) 
    node2 = ListNode(2)  
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


sol = Solution()
ansNode = sol.reverseBetween(node1, 3, 4)
print(f"{ansNode}")