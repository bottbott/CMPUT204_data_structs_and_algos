import sys
import os
from node import BFSNode
sys.path.append(os.path.abspath('/Users/ryanbott/Projects/CMPUT204_data_structs_and_algos/DataStructures')) 
sys.path.append(os.path.abspath('/Users/ryanbott/Projects/CMPUT204_data_structs_and_algos/ADT')) 
from ryan_queue import Queue
from typing import List

class Edge:
    def __init__(self, start, end, weight=None):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, vertices: List[BFSNode]):
        self.vertices = vertices
        vertex: BFSNode
        self.adj_list = {vertex.key: [] for vertex in vertices}
        self.adj_matrix = [[0 for vertex in vertices] for vertex in vertices]

    def add_edge(self, edge: Edge, weight=None) -> None:
        self.adj_list[edge.start].append(edge.end)
        self.adj_matrix[self.vertices.index(BFSNode(edge.start, None))][self.vertices.index(BFSNode(edge.end, None))] = 1 if weight == None else weight

    def get_adj_list(self):
        return self.adj_list
    
    def get_adj_matrix(self):
        return self.adj_matrix
    
    def bfs(self, source: BFSNode):
        bfs_vertices = []
        bfs_edges = []
        for v in self.vertices:
            node = BFSNode(v.key, v.data)
            node.color = 'White'
            node.dist = sys.maxsize
            bfs_vertices.append(node)
        queue = Queue()
        source.color = 'White'
        source.dist = 0
        queue.enqueue(source)
        while (not queue.is_empty()):
            origin: BFSNode = queue.dequeue()
            neighbour: BFSNode
            for neighbour in self.adj_list[origin.key]:
                if (bfs_vertices[neighbour].color == 'White'):
                    bfs_vertices[neighbour].color = 'Grey'
                    bfs_vertices[neighbour].dist = origin.dist + 1
                    bfs_vertices[neighbour].predecessesor = origin
                    bfs_edges.append(Edge(origin.key, bfs_vertices[neighbour].key))
                    queue.enqueue(bfs_vertices[neighbour])
            origin.color = 'Black'
        return bfs_edges
    
    def print(self):
        # print adjacency list representation
        for vertex, adj_list in self.adj_list.items():
            print(vertex, "->", adj_list)
        print()

        # print adjacency matrix representation
        max_vert = len(str(len(self.vertices)))
        print(" ", end=" " * (max_vert + max_vert - 1))
        for vertex in self.vertices:
            print(vertex.key, end=" " * (max_vert))
        print()
        
        for i in range(len(self.vertices)):
            print(self.vertices[i].key, end=" " * (max_vert + max_vert - len(str(i+1))))
            # print(self.vertices[i].key, end=" " * (max_vert-len(str(i))))
            for j in range(len(self.vertices)):
                print(int(self.adj_matrix[i][j]), end=" " * max_vert)
            print()
        



