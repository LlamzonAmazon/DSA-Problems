class Node:
    def __init__(self, key, val):
        self.key = key # Used to identify node when evisting LRU
        self.value = val # Used to retrieve node's value for get()
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map keys to nodes

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def evict(self, node):
        prev, nxt = node.prev, node.next # Store original pointers
        prev.next, nxt.prev = nxt, prev # Point left and right at each other

    def insert(self, node):
        
        nodeLeft, nodeRight = self.right.prev, self.right # Store original node pointers
        nodeLeft.next = nodeRight.prev = node # Point left and right at node
        node.next, node.prev = nodeRight, nodeLeft # Point node at left and right

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        self.evict(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value


    def put(self, key: int, value: int) -> None:

        # Update value by eviction & insertion to ensure recency pointers stay updated
        if key in self.cache:
            self.evict(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If cache is at capacity, evict LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.evict(lru)
            del self.cache[lru.key]

        

