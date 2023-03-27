from queue import Queue
from queue import PriorityQueue
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w=0):
        self.adjacency_list[u].append((v, w))
        self.adjacency_list[v].append((u, w))

    def dfs(self, start):
        visited = [False] * self.vertices
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor[0]]:
                self._dfs(neighbor[0], visited)

    def bfs(self, start):
        visited = [False] * self.vertices
        q = Queue()
        q.put(start)
        visited[start] = True
        while not q.empty():
            vertex = q.get()
            print(vertex, end=' ')
            for neighbor in self.adjacency_list[vertex]:
                if not visited[neighbor[0]]:
                    q.put(neighbor[0])
                    visited[neighbor[0]] = True

    def dijkstra(self, start):
        distances = [float('inf')] * self.vertices
        distances[start] = 0
        pq = PriorityQueue()
        pq.put((0, start))
        while not pq.empty():
            current_distance, current_vertex = pq.get()
            if current_distance > distances[current_vertex]:
                continue
            for neighbor in self.adjacency_list[current_vertex]:
                distance = current_distance + neighbor[1]
                if distance < distances[neighbor[0]]:
                    distances[neighbor[0]] = distance
                    pq.put((distance, neighbor[0]))
        return distances

    def kruskal(self):
        edges = []
        for vertex in range(self.vertices):
            for neighbor in self.adjacency_list[vertex]:
                edges.append((vertex, neighbor[0], neighbor[1]))
        edges.sort(key=lambda x: x[2])
        parent = list(range(self.vertices))
        rank = [0] * self.vertices
        mst = []
        for edge in edges:
            u, v, weight = edge
            u_parent = self._find(parent, u)
            v_parent = self._find(parent, v)
            if u_parent != v_parent:
                mst.append(edge)
                if rank[u_parent] > rank[v_parent]:
                    parent[v_parent] = u_parent
                else:
                    parent[u_parent] = v_parent
                    if rank[u_parent] == rank[v_parent]:
                        rank[v_parent] += 1
        return mst

    def prim(self):
        visited = [False] * self.vertices
        distances = [float('inf')] * self.vertices
        parent = [None] * self.vertices
        distances[0] = 0
        pq = PriorityQueue()
        pq.put((0, 0))
        while not pq.empty():
            current_distance, current_vertex = pq.get()
            visited[current_vertex] = True
            for neighbor in self.adjacency_list[current_vertex]:
                if not visited[neighbor[0]]:
                    distance = neighbor[1]
                    if distance < distances[neighbor[0]]:
                        distances[neighbor[0]] = distance
                        parent[neighbor[0]] = current_vertex
                        pq.put((distance, neighbor[0]))
        mst = []
        for i in range(1, self.vertices):
            mst.append((parent[i], i, distances[i]))
        return mst

    def floyd_warshall(self):
        distances = [[float('inf')]*self.vertices for _ in range(self.vertices)]
        for i in range(self.vertices):
            distances[i][i] = 0
        for vertex in range(self.vertices):
            for neighbor in self.adjacency_list[vertex]:
                distances[vertex][neighbor[0]] = neighbor[1]
        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        return distances

    def _find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self._find(parent, parent[vertex])
        return parent[vertex]
                    
                    
