import heapq

class TreeNode:
    def __init__(self, node, parent=None):
        self.node = node
        self.parent = parent

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def greedy_tree_search(self, start, goal, heuristics):
        visited = set()
        priority_queue = [TreeNode(start)]

        while priority_queue:
            current_node = priority_queue.pop(0)
            node = current_node.node

            if node not in visited:
                visited.add(node)
                print(node, end=' ')

                if node == goal:
                    return  # Reached the goal

                if node in self.graph:
                    # Create child nodes for unvisited neighbors
                    for neighbor, _ in self.graph[node]:
                        if neighbor not in visited:
                            child_node = TreeNode(neighbor, current_node)
                            priority_queue.append(child_node)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('S', 'A', 3)
    graph.add_edge('S', 'B', 3)
    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 3)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'G', 4)
    graph.add_edge('D', 'G', 3)

    heuristics = {
        'S': 7,
        'A': 5,
        'B': 7,
        'C': 4,
        'D': 1,
        'G': 0
    }

    print("Greedy Best-First Tree Search (from 'S' to 'G'):")
    graph.greedy_tree_search('S', 'G', heuristics)
