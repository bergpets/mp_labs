from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def tarjan_topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.tarjan_topological_sort_util(i, visited, stack)
        return stack[::-1]

    def tarjan_topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.tarjan_topological_sort_util(i, visited, stack)
        stack.append(v)

    def fleury(self):
        if self.has_odd_degree():
            return "Graph is not Eulerian"
        else:
            return self.fleury_util(0)

    def fleury_util(self, u):
        for v in self.graph[u]:
            if self.is_valid_next_edge(u, v):
                self.remove_edge(u, v)
                return str(u) + "-" + str(v) + " " + self.fleury_util(v)
        return ""

    def has_odd_degree(self):
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                return True
        return False

    def is_valid_next_edge(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        else:
            visited = [False] * self.V
            count1 = self.dfs_count(u, visited)
            self.remove_edge(u, v)
            visited = [False] * self.V
            count2 = self.dfs_count(u, visited)
            self.add_edge(u, v)
            return False if count1 > count2 else True

    def dfs_count(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.dfs_count(i, visited)
        return count

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def kosaraju(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)
        gr = self.get_transpose()
        visited = [False] * self.V
        result = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                temp = []
                gr.dfs_util(i, visited, temp)
                result.append(temp)
        return result

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)

    def get_transpose(self):
        g = Graph(self.V)
        for i in range(self.V):
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def dfs_util(self, v, visited, temp):
        visited[v] = True
        temp.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited, temp)
                
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Tarjan Topological Sort: ", g.tarjan_topological_sort())
print("Fleury: ", g.fleury())
print("Kosaraju: ", g.kosaraju())