class LRUCache:

    class Node:
        def __init__(self, val=None, next=None, prev=None, key=None):
            self.val = val
            self.next = next
            self.prev = prev
            self.key = key

    def __init__(self, capacity: int):
        self.h = {}
        self.capacity = capacity
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def pushToFront(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.h:
            node = self.h[key]
            self.pushToFront(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            node = self.h[key]
            node.val = value
            self.pushToFront(node)

        else:
            if len(self.h) + 1 <= self.capacity:
                node = self.Node(
                    key=key, 
                    val=value, 
                    next=self.head.next, 
                    prev=self.head)
                self.head.next = node
                node.next.prev = node
                self.h[key] = node
            else:
                node = self.tail.prev
                del self.h[node.key] # delete last item
                
                node.val = value
                node.key = key
                self.pushToFront(node)
                self.h[key] = node
                
        


