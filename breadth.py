from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)

            if node not in visited:
                print(node, end=' ')
                visited.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('S', 'A')
    graph.add_edge('S', 'B')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'G')
    

    print("Breadth First Traversal (starting from vertex S):")
    graph.bfs('S')
