from collections import defaultdict

class TreeNode:
    def __init__(self, node, parent=None):
        self.node = node
        self.parent = parent

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_tree_search(self, start):
        visited = set()
        queue = [TreeNode(start)]

        while queue:
            current_node = queue.pop(0)
            node = current_node.node

            if node not in visited:
                visited.add(node)
                print(node, end=' ')

                if node in self.graph:
                    # Create child nodes for unvisited neighbors
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            child_node = TreeNode(neighbor, current_node)
                            queue.append(child_node)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('S', 'A')
    graph.add_edge('S', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'F')
    graph.add_edge('D', 'F')

    print("Breadth First Tree Search (starting from vertex S):")
    graph.bfs_tree_search('S')
