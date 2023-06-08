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

    # how can I implement eq or something so that I can check if an EDGE is IN a collection? 
    # tried this below but got "unhashable type" 'Edge'
    def __eq__(self, __value: object) -> bool:
        return self.start == __value.start and self.end == __value.end
    
    def __hash__(self) -> int:
        return self.start * self.end
    
    def __repr__(self) -> str:
        return f"({self.start}, {self.end})"

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
    
    def bfs(self, key):
        bfs_vertices = []
        bfs_edges = []
        for v in self.vertices:
            node = BFSNode(v.key, v.data)
            node.color = 'White'
            node.dist = sys.maxsize
            bfs_vertices.append(node)
        queue = Queue()
        bfs_vertices[key].color = 'Grey'
        bfs_vertices[key].dist = 0
        # source.color = 'White'
        # source.dist = 0
        # an issue here is that the source node is living outside of the self.vertices ecosystem. 
        # we need to use that particular node from the vertices. maybe we should pass in the key?
        queue.enqueue(bfs_vertices[key])
        while (not queue.is_empty()):
            origin: BFSNode = queue.dequeue()
            neighbour: BFSNode
            for neighbour in self.adj_list[origin.key]:
                neighbour = neighbour - 1
                if (bfs_vertices[neighbour].color == 'White'):
                    bfs_vertices[neighbour].color = 'Grey'
                    bfs_vertices[neighbour].dist = origin.dist + 1
                    bfs_vertices[neighbour].predecessesor = origin.key
                    bfs_edges.append(Edge(origin.key, bfs_vertices[neighbour].key))
                    queue.enqueue(bfs_vertices[neighbour])
            origin.color = 'Black'
        return bfs_edges
    
    def dfs_visit(self, source: BFSNode, dfs_edges: List[Edge], dfs_vertices: List[BFSNode], time):
        time = time + 1
        source.color = 'Grey'
        source.time = time
        # neighbour: Number
        for neighbour in self.adj_list[source.key]: # these are just ints
            neighbour = neighbour
            if dfs_vertices[neighbour-1].color == 'White':
                dfs_edges.append(Edge(source.key, neighbour))
                dfs_vertices[neighbour-1].predecessesor = source
                self.dfs_visit(dfs_vertices[neighbour-1], dfs_edges, dfs_vertices, time)
            source.color = 'Black'
            time = time + 1
            source.ftime = time
    
    def dfs(self):
        dfs_vertices = []
        dfs_edges = []
        time = 0
        for v in self.vertices:
            node = BFSNode(v.key, v.data)
            node.color = 'White'
            node.dist = sys.maxsize
            dfs_vertices.append(node)
        v: BFSNode
        for v in dfs_vertices:
            if v.color == 'White':
                self.dfs_visit(v, dfs_edges, dfs_vertices, time)
        return dfs_edges
    


    
    def print(self):
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
        # print adjacency list representation
        for vertex, adj_list in self.adj_list.items():
            print(vertex, "->", adj_list)
        print()
        



