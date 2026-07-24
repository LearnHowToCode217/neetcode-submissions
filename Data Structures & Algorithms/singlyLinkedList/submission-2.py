class ListNode:
    def __init__(self,val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self): # Creating Dummy Node
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next # because the previous is a dummy Node --> self.head.next point at the first val
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
                
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
