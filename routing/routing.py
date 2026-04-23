import networkx as nx
import time

def run_dijkstra(graph, source, target):
    start = time.time()

    path = nx.shortest_path(graph, source=source, target=target, weight="length")
    length = nx.shortest_path_length(graph, source=source, target=target, weight="length")

    end = time.time()

    return {
        "path": path,
        "length": length,
        "time": end - start,
        "nodes_in_path": len(path)
    }