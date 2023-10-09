import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def greedy_search(self, start, goal, heuristics):
        visited = set()
        priority_queue = [(heuristics[start], start)]

        while priority_queue:
            _, node = heapq.heappop(priority_queue)

            if node not in visited:
                print(node, end=' ')
                visited.add(node)

                if node == goal:
                    return  # Reached the goal

                if node in self.graph:
                    for neighbor, _ in self.graph[node]:
                        if neighbor not in visited:
                            heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

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

    heuristics = {
        'S': 7,
        'A': 5,
        'B': 7,
        'C': 4,
        'D': 1,
        'G': 0
    }

    print("Greedy Best-First Search (from 'S' to 'G'):")
    graph.greedy_search('S', 'G', heuristics)
