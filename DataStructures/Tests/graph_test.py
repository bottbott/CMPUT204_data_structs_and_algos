import sys
import os
import random
sys.path.append(os.path.abspath('/Users/ryanbott/Projects/CMPUT204_data_structs_and_algos/DataStructures')) 

from node import BFSNode
from graph import Graph, Edge

n = 8#10 # vertices
m = 20#15 # edges

vertices = list(range(1, n+1)) # node keys from 1 to n+1
edges = set()

while len(edges) < m:
    u = random.choice(vertices)
    v = random.choice(vertices)
    if u != v and Edge(u, v) not in edges:
        edge = Edge(u, v)
        edges.add(edge) 

nodes = [BFSNode(key, key) for key in vertices]

graph = Graph(nodes) # maybe this should take an argument of edges as well? 
for edge in edges: 
    graph.add_edge(edge)

graph.print()

print(nodes[0])
print([e for e in graph.bfs(0)])
print([e for e in graph.dfs()])