class TreeNode:
    def __init__(self, node, parent=None):
        self.node = node
        self.parent = parent

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_tree_search(self, start):
        visited = set()
        stack = [TreeNode(start)]

        while stack:
            current_node = stack.pop()
            node = current_node.node

            if node not in visited:
                visited.add(node)
                print(node, end=' ')

                if node in self.graph:
                    # Create child nodes for unvisited neighbors
                    for neighbor in reversed(self.graph[node]):
                        if neighbor not in visited:
                            child_node = TreeNode(neighbor, current_node)
                            stack.append(child_node)

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

    print("Depth First Tree Search (starting from vertex S):")
    graph.dfs_tree_search('S')
