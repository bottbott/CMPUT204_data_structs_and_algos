import sys
import os
from node import BFSNode
sys.path.append(os.path.abspath('/Users/ryanbott/LocalDocs/School/CMPUT 204/Code/ADT')) 
from ryan_queue import Queue

class Edge:
    def __init__(self, start, end, weight=None):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}
        self.adj_matrix = [[0 for vertex in vertices] for vertex in vertices]

    def add_edge(self, edge: Edge, weight=None) -> None:
        self.adj_list[edge.start].append(edge.end)
        self.adj_matrix[self.vertices.index(edge.start)][self.vertices.index(edge.end)] = 1 if weight == None else weight

    def get_adj_list(self):
        return self.adj_list
    
    def get_adj_matrix(self):
        return self.adj_matrix
    
    def bfs(self, source: BFSNode):
        bfs_vertices = []
        for v in self.vertices:
            node = BFSNode()
            node.color = 'White'
            node.dist = sys.maxsize
            bfs_vertices.append(node)
        queue = Queue()
        source.color = 'White'
        source.dist = 0
        queue.queue(source)
        while (not queue.empty()):
            origin: BFSNode = queue.dequeue()
            neighbour: BFSNode
            for neighbour in self.adj_list[origin]:
                if (neighbour.color == 'White'):
                    neighbour.color = 'Grey'
                    neighbour.dist = origin.dist + 1
                    neighbour.predecessesor = origin
                    bfs_vertices.append(Edge(origin.key, neighbour.key))
                    queue.enqueue(neighbour)
            origin.color = 'Black'
        return bfs_vertices
        



