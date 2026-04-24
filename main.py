import osmnx as ox
import networkx as nx
import random

from pipeline.preprocessing import preprocess_graph
from pipeline.topology_cleaning import clean_graph
from routing.routing import (
    initialize_edge_features,
    update_traffic,
    run_routing
)
from analysis.benchmark import compare_routes


def get_largest_component(G):
    largest_cc = max(nx.connected_components(G), key=len)
    return G.subgraph(largest_cc).copy()


def main():
    print("Downloading graph...")

    G = ox.graph_from_point(
        (30.3165, 78.0322),
        dist=1000,
        network_type="drive",
        simplify=False
    )

    print("Preprocessing...")
    G = preprocess_graph(G)

    print("Cleaning...")
    G = clean_graph(G)

    print("Ensuring connectivity...")
    G = get_largest_component(G)

    print("Initializing edge features...")
    G = initialize_edge_features(G)

    nodes = list(G.nodes)
    source, target = random.sample(nodes, 2)

    print("Running normal traffic routing...")
    normal_results = compare_routes(G, source, target, run_routing)

    print("Updating to peak traffic...")
    update_traffic(G, peak=True)

    print("Running peak traffic routing...")
    peak_results = compare_routes(G, source, target, run_routing)

    print("\n--- NORMAL TRAFFIC ---")
    for k, v in normal_results.items():
        print(k, ":", v)

    print("\n--- PEAK TRAFFIC ---")
    for k, v in peak_results.items():
        print(k, ":", v)


if __name__ == "__main__":
    main()