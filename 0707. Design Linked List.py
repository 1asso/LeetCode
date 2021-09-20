class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy_head = Node()
        self.count = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.count - 1:
            return -1
        cur = self.dummy_head
        for i in range(index + 1):
            cur = cur.next
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = Node(val)
        new.next = self.dummy_head.next
        self.dummy_head.next = new
        self.count += 1
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.count += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        new = Node(val)
        new.next = cur.next
        cur.next = new
        self.count += 1
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.count - 1:
            return
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.count -= 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)