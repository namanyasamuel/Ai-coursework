import heapq

class TreeNode:
    def __init__(self, node, parent=None, cost=0):
        self.node = node
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        # Define comparison for heapq based on f-value
        return self.cost < other.cost

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def astar_search(self, start, goal, heuristics):
        visited = set()
        priority_queue = [TreeNode(start)]  # Start with the root node

        while priority_queue:
            current_node = heapq.heappop(priority_queue)

            if current_node.node not in visited:
                visited.add(current_node.node)
                print(current_node.node, end=' ')

                if current_node.node == goal:
                    return  # Reached the goal

                if current_node.node in self.graph:
                    for neighbor, edge_cost in self.graph[current_node.node]:
                        if neighbor not in visited:
                            g_neighbor = current_node.cost + edge_cost
                            f_neighbor = g_neighbor + heuristics[neighbor]
                            heapq.heappush(priority_queue, TreeNode(neighbor, current_node, g_neighbor))

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph = Graph()
    graph.add_edge('S', 'A', 3)
    graph.add_edge('S', 'B', 1)
    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 3)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'G', 4)
    graph.add_edge('D', 'G', 1)

    heuristics = {
        'S': 7,
        'A': 5,
        'B': 7,
        'C': 4,
        'D': 1,
        'G': 0
    }

    print("A* Tree Search (from 'S' to 'G'):")
    graph.astar_search('S', 'G', heuristics)
