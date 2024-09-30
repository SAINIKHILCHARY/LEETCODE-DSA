import heapq


def prims_algorithm(graph, start_vertex):
    # List to store the edges of the Minimum Spanning Tree (MST)
    mst_edges = []

    # Set to track visited vertices
    visited = set()

    # Min-heap to pick the edge with the minimum weight
    min_heap = [(0, start_vertex, None)]  # (edge weight, vertex, from vertex)

    while min_heap:
        # Pop the minimum weight edge
        weight, current_vertex, from_vertex = heapq.heappop(min_heap)

        # If the current vertex is already visited, skip it
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # If there is a valid from_vertex (i.e., not None), add the edge to the MST
        if from_vertex is not None:
            mst_edges.append((from_vertex, current_vertex, weight))

        # Add all neighboring vertices that are not visited to the heap
        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return mst_edges


# Example Usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 3)],
        'B': [('A', 4), ('C', 1), ('D', 2)],
        'C': [('A', 3), ('B', 1), ('D', 4)],
        'D': [('B', 2), ('C', 4)]
    }

    start_vertex = 'A'
    mst = prims_algorithm(graph, start_vertex)
    print("Minimum Spanning Tree edges:", mst)
