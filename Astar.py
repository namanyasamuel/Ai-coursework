import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def astar_search(self, start, goal, heuristics):
        visited = set()
        priority_queue = [(heuristics[start], 0, start)]  # (f = g + h, g, node)

        while priority_queue:
            _, g, node = heapq.heappop(priority_queue)

            if node not in visited:
                print(node, end=' ')
                visited.add(node)

                if node == goal:
                    return  # Reached the goal

                if node in self.graph:
                    for neighbor, edge_cost in self.graph[node]:
                        if neighbor not in visited:
                            g_neighbor = g + edge_cost
                            f_neighbor = g_neighbor + heuristics[neighbor]
                            heapq.heappush(priority_queue, (f_neighbor, g_neighbor, neighbor))

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

    print("A* Search (from 'S' to 'G'):")
    graph.astar_search('S', 'G', heuristics)
