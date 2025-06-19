from typing import Optional

class ListNode:
    def __init__(self, val: int, prev: Optional['ListNode'] = None, next: Optional['ListNode'] = None):
        self.val = val
        self.prev = prev        # Only for doubly-linked Lists
        self.next = next
        
    def __repr__(self):
        return (f"<ListNode val={self.val} "
                f"at address {hex(id(self))} "
                f"\nprev={hex(id(self.prev)) if self.prev else None}, "
                f"\nnext={hex(id(self.next)) if self.next else None}>")
        
    def add_node(self, node_to_add: 'ListNode'): # Given Linked List = [0,1,2] & adding node w/ value(4) at position 1      
        prev_node: Optional['ListNode'] = self.prev   
        node_to_add.next = self                
        node_to_add.prev = prev_node
        prev_node.next = node_to_add #type:ignore
        self.prev = node_to_add     
        
    def delete_node(self):
        prev_node, next_node = self.prev, self.next
        prev_node = next_node.prev #type:ignore
        next_node = prev_node.next #type:ignore
            
if __name__ == "__main__":
    node1 = ListNode(1)
    print(node1)