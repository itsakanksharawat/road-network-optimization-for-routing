import os
import time
import osmnx as ox

# -------------------------
# CONFIG
# -------------------------
INPUT_PATH = "data/processed/preprocessed.graphml"
OUTPUT_DIR = "data/cleaned"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_PATH = os.path.join(OUTPUT_DIR, "dehradun_cleaned.graphml")

MIN_EDGE_LENGTH = 5.0  # meters

# -------------------------
# Load graph
# -------------------------
start = time.time()

print("[INFO] Loading preprocessed graph...")
G = ox.load_graphml(INPUT_PATH)

before_nodes = len(G.nodes)
before_edges = len(G.edges)

print(f"[INFO] Nodes before: {before_nodes}")
print(f"[INFO] Edges before: {before_edges}")

# -------------------------
# 1️⃣ Remove micro edges
# -------------------------
print("[INFO] Removing micro edges...")

edges_to_remove = [
    (u, v, k)
    for u, v, k, d in G.edges(keys=True, data=True)
    if d.get("length", 0) < MIN_EDGE_LENGTH
]

G.remove_edges_from(edges_to_remove)

print(f"[INFO] Removed {len(edges_to_remove)} micro edges")

# -------------------------
# 2️⃣ Simplify degree-2 nodes (CORE LOGIC)
# -------------------------
print("[INFO] Simplifying degree-2 nodes...")

def simplify_degree_2_nodes(G):
    nodes = list(G.nodes())

    for node in nodes:
        if node not in G:
            continue

        # Only process nodes with exactly 2 connections
        if G.degree(node) != 2:
            continue

        neighbors = list(G.neighbors(node))

        if len(neighbors) != 2:
            continue

        u, v = neighbors

        # Avoid self-loop
        if u == v:
            continue

        # Get edge data
        data1 = G.get_edge_data(node, u)
        data2 = G.get_edge_data(node, v)

        if not data1 or not data2:
            continue

        # Compute combined length
        length = 0
        for k in data1:
            length += data1[k].get("length", 0)
        for k in data2:
            length += data2[k].get("length", 0)

        # Add merged edge
        G.add_edge(u, v, length=length)

        # Remove node
        G.remove_node(node)

    return G

G = simplify_degree_2_nodes(G)

# -------------------------
# 3️⃣ Remove isolated nodes (cleanup)
# -------------------------
print("[INFO] Removing isolated nodes...")

isolated = list(ox.isolated_nodes(G))
G.remove_nodes_from(isolated)

print(f"[INFO] Removed {len(isolated)} isolated nodes")

# -------------------------
# Save cleaned graph
# -------------------------
ox.save_graphml(G, OUTPUT_PATH)

after_nodes = len(G.nodes)
after_edges = len(G.edges)

end = time.time()

# -------------------------
# Final Results
# -------------------------
print("\n[SUCCESS] CLEANING COMPLETE")
print(f"Nodes: {before_nodes} → {after_nodes}")
print(f"Edges: {before_edges} → {after_edges}")
print(f"Time taken: {round(end - start, 2)} sec")
   

    

