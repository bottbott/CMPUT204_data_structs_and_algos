class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data

class GraphNode(Node):
    def __init__(self, data):
        super().__init__(data)

class BFSNode(GraphNode):
    def __init__(self, key, data):
        super().__init__(key, data)
        self.color = None
        self.dist = None
        self.predecessesor = None

class TreeNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.left = None
        self.right = None

class LinkedListNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None

class DblLinkedListNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None
        self.prev = None