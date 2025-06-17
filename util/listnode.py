from typing import Optional

class ListNode:
    def __init__(self, val: int, prev: Optional['ListNode'] = None, next: Optional['ListNode'] = None):
        self.val = val
        self.prev = prev        # Only for doubly-linked Lists
        self.next = next
        
    def __repr__(self):
        return (f"<ListNode var={self.val} "
                f"at {hex(id(self))} | "
                f"prev={hex(id(self.prev)) if self.prev else None}, "
                f"next={hex(id(self.next)) if self.next else None}>")