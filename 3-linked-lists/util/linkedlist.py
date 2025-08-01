from typing import Optional, Iterator
from .listnode import ListNode

class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        
    def append(self, val: int) -> ListNode:
        new_node = ListNode(val)
        
        if not self.head:                           # if self.head has no value
            self.head = self.tail = new_node        
        else:
            self.tail.next = new_node # type: ignore
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    
    def __iter__(self) -> Iterator[ListNode]:
        curr = self.head
        while curr:
            yield curr                              # Generate a value on-demand
            curr = curr.next
    
    def print_list(self):
        for node in self:
            print(node)