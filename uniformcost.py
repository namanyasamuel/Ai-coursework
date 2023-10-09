import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def ucs(self, start, goal):
        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)

            if node not in visited:
                print(node, end=' ')
                visited.add(node)

                if node == goal:
                    return  # Reached the goal

                if node in self.graph:
                    for neighbor, edge_cost in self.graph[node]:
                        if neighbor not in visited:
                            new_cost = cost + edge_cost
                            heapq.heappush(priority_queue, (new_cost, neighbor))

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('S', 'A', 3)
    graph.add_edge('S', 'B', 1)
    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 3)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'G', 4)
    graph.add_edge('D', 'G', 1)

    print("Uniform Cost Search (from 'S' to 'G'):")
    graph.ucs('S', 'G')
