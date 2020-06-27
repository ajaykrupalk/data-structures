from collections import defaultdict
graph=defaultdict(list)#holds key:value pair 

def addEdge(graph,u,v):
  graph[u].append(v)

def generate_edges(graph):
  edges=[]
  for node in graph:
    for neighbour in graph[node]:
      edges.append((node,neighbour))
  return edges

addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
print(generate_edges(graph))
