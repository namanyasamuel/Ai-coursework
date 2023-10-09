

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=' ')
                visited.add(node)

            if node in self.graph:
                # Push unvisited neighbors onto the stack
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

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
    graph.add_edge('D','G')


    print("Depth First Traversal (starting from vertex S):")
    graph.dfs('S')

