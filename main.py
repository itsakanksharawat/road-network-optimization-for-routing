import osmnx as ox
import networkx as nx
import random

from pipeline.preprocessing import preprocess_graph
from pipeline.topology_cleaning import clean_graph
from routing.routing import run_dijkstra
from analysis.benchmark import compare_graphs
from analysis.validation import validate_paths

# NEW IMPORT
from visualization.plot_graph import plot_graph, plot_graph_with_path


def get_largest_component(G):
    largest_cc = max(nx.connected_components(G), key=len)
    return G.subgraph(largest_cc).copy()


def main():
    print("Downloading graph...")

    # Smaller region for smooth visualization
    raw_graph = ox.graph_from_point(
        (30.3165, 78.0322),
        dist=1000,
        network_type="drive",
        simplify=False
    )

    print("Preprocessing...")
    processed_graph = preprocess_graph(raw_graph)

    # ✅ VISUAL 1 — RAW GRAPH
    print("Visualizing raw graph...")
    plot_graph(processed_graph, "Raw Graph")

    print("Cleaning topology...")
    cleaned_graph = clean_graph(processed_graph.copy())

    # ✅ VISUAL 2 — CLEAN GRAPH
    print("Visualizing cleaned graph...")
    plot_graph(cleaned_graph, "Cleaned Graph")

    # Ensure connectivity
    processed_graph = get_largest_component(processed_graph)
    cleaned_graph = get_largest_component(cleaned_graph)

    nodes = list(cleaned_graph.nodes)

    if len(nodes) < 2:
        print("Graph too small after cleaning.")
        return

    source, target = random.sample(nodes, 2)

    print("Running benchmark...")

    raw_res, clean_res, comp = compare_graphs(
        processed_graph,
        cleaned_graph,
        source,
        target,
        run_dijkstra
    )

    # ✅ VISUAL 3 — PATHS (MOST IMPORTANT)
    print("Visualizing paths...")
    plot_graph_with_path(processed_graph, raw_res["path"], "Raw Graph Path")
    plot_graph_with_path(cleaned_graph, clean_res["path"], "Clean Graph Path")

    validation = validate_paths(raw_res, clean_res)

    print("\n--- RAW GRAPH ---")
    print(raw_res)

    print("\n--- CLEAN GRAPH ---")
    print(clean_res)

    print("\n--- COMPARISON ---")
    print(comp)

    print("\n--- VALIDATION ---")
    print(validation)


if __name__ == "__main__":
    main()
    