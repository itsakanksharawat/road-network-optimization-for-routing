import os
import json
import osmnx as ox
import statistics

# -----------------------
# Paths
# -----------------------
RAW_PATH = "data/raw/dehradun_raw.graphml"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

# -----------------------
# Load raw graph
# -----------------------
print("[INFO] Loading raw graph...")
G = ox.load_graphml(RAW_PATH)

# -----------------------
# Convert to undirected (important for simplification)
# -----------------------
print("[INFO] Converting to undirected graph...")
G = ox.utils_graph.get_undirected(G)

# -----------------------
# Remove isolated nodes
# -----------------------
print("[INFO] Removing isolated nodes...")
G.remove_nodes_from(list(ox.isolated_nodes(G)))

# -----------------------
# Compute stats (NOW useful)
# -----------------------
num_nodes = len(G.nodes)
num_edges = len(G.edges)

degrees = [deg for _, deg in G.degree()]
edge_lengths = [
    data["length"]
    for _, _, data in G.edges(data=True)
    if "length" in data
]

stats = {
    "nodes": num_nodes,
    "edges": num_edges,
    "avg_degree": round(statistics.mean(degrees), 2),
    "max_degree": max(degrees),
    "avg_edge_length": round(statistics.mean(edge_lengths), 2),
    "min_edge_length": round(min(edge_lengths), 2),
    "max_edge_length": round(max(edge_lengths), 2),
}

# -----------------------
# Save stats
# -----------------------
stats_path = os.path.join(PROCESSED_DIR, "preprocessing_stats.json")
with open(stats_path, "w") as f:
    json.dump(stats, f, indent=4)

print(f"[INFO] Stats saved at: {stats_path}")

# -----------------------
# Save cleaned graph (IMPORTANT)
# -----------------------
processed_graph_path = os.path.join(PROCESSED_DIR, "preprocessed.graphml")
ox.save_graphml(G, processed_graph_path)

print(f"[INFO] Preprocessed graph saved at: {processed_graph_path}")

print("[SUCCESS] Step 2 (Preprocessing) completed.")
