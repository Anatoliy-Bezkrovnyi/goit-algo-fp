import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.distance = float('inf')
        self.visited = False

def dijkstra(graph, start_node):
    heap = []
    start_node.distance = 0
    heapq.heappush(heap, (start_node.distance, start_node))
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        current_node.visited = True
        
        for neighbor, edge_weight in graph[current_node]:
            neighbor_distance = current_dist + edge_weight
            
            if neighbor_distance < neighbor.distance:
                neighbor.distance = neighbor_distance
                heapq.heappush(heap, (neighbor.distance, neighbor))
