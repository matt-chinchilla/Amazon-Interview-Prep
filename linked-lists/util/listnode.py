from typing import Optional

class ListNode:
    def __init__(self, val: int, prev: Optional['ListNode'] = None, next: Optional['ListNode'] = None):
        self.val = val
        self.prev = prev        # Only for doubly-linked Lists
        self.next = next
        
    def __repr__(self):
        return (f"<ListNode val={self.val} "
                f"\nat address {hex(id(self))} | "
                f"\nprev={hex(id(self.prev)) if self.prev else None}, "
                f"\nnext={hex(id(self.next)) if self.next else None}>")
        
if __name__ == "__main__":
    node1 = ListNode(1)
    print(node1)