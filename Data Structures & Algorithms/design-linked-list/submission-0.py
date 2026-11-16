
class LinkedListNode:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


class MyLinkedList:

    def __init__(self):
        self.right = LinkedListNode(0)
        self.left = LinkedListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0 and cur != self.right:
            return cur.val

        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = LinkedListNode(val), self.left, self.left.next

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, prev, next = LinkedListNode(val), self.right.prev, self.right

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            node, prev, next = LinkedListNode(val), cur.prev, cur

            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0 and cur != self.right:
            prev, next = cur.prev, cur.next

            prev.next = next
            next.prev = prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)