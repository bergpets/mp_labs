from graph_a import Graph
g = Graph(5)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 4)

print("DFS:")
g.dfs(0)
print()

print("BFS:")
g.bfs(0)
print()

print("Dijkstra:")
print(g.dijkstra(0))

print("Kruskal:")
print(g.kruskal())

print("Prim:")
print(g.prim())

print("Floyd-Warshall:")
print(g.floyd_warshall())