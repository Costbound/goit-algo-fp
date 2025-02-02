import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        heap = [(0, start)]
        distances = {start: 0}
        visited = set()

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

if __name__ == '__main__':
    # Example usage
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_node = 'A'
    distances = graph.dijkstra(start_node)

    print(f"Shortest distances from {start_node}:")
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")