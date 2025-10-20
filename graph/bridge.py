from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.edges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges.append((u, v))

    def is_connected(self):
        visited = [False] * self.V
        start = 0
        q = deque([start])
        visited[start] = True

        while q:
            u = q.popleft()
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return all(visited)

    def find_bridges(self):
        bridges = []
        for u, v in self.edges:
            # Remove edge (u, v)
            self.graph[u].remove(v)
            self.graph[v].remove(u)

            if not self.is_connected():
                bridges.append((u, v))

            # Add edge back
            self.graph[u].append(v)
            self.graph[v].append(u)
        return bridges

class Graph2:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _dfs(self, u, visited, parent, disc, low, bridges, time):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self._dfs(v, visited, parent, disc, low, bridges, time)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [-1] * self.V
        bridges = []
        time = [0]

        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, parent, disc, low, bridges, time)
        return bridges


# Example usage:
if __name__ == "__main__":
    ###
    ###
      #   4
      #   |
      #   3
      #   |
      #   0
      #  / \
      # 1---2
    ###
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    bridges = g.find_bridges()
    print("Bridges in the graph:", bridges)

    g = Graph2(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    bridges = g.find_bridges()
    print("Bridges in the graph:", bridges)
