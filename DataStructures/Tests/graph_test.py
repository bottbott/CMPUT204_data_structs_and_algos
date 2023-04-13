import sys
import os
import random
sys.path.append(os.path.abspath('/Users/ryanbott/LocalDocs/School/CMPUT 204/Code/DataStructures')) 

from node import BFSNode
from graph import Graph, Edge

n = 10 # vertices
m = 15 # edges

vertices = list(range(1, n+1))
edges = set()

while len(edges) < m:
    u = random.choice(vertices)
    v = random.choice(vertices)
    if u != v:
        edge = Edge(u, v)
        edges.add(edge) 

nodes = [BFSNode(key, key) for key in vertices]

graph = Graph(nodes)
for edge in edges: 
    graph.add_edge(edge)