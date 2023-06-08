class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __eq__(self, __value: object) -> bool:
        return self.key == __value.key
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    
    def __repr__(self) -> str:
        return f"Key: {self.key}. Value: {self.data}"

class GraphNode(Node):
    def __init__(self, key, data):
        super().__init__(key, data)

class BFSNode(GraphNode):
    def __init__(self, key, data):
        super().__init__(key, data)
        self.color = None
        self.dist = None
        self.predecessesor = None
        self.stime = None
        self.ftime = None
    def __repr__(self) -> str:
        return f"Key: {self.key}. Value: {self.data}. Color: {self.color}. Pred: {self.predecessesor}. Dist: {self.dist}. Time: {self.stime}, {self.ftime}."
    
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