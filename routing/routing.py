import networkx as nx
import time
import random

# ---------- EDGE FEATURE INITIALIZATION ----------

def initialize_edge_features(G):
    for u, v, data in G.edges(data=True):
        distance = data.get("length", 1)

        # assume default speed (km/h)
        speed = data.get("speed_kph", 40)

        # convert to m/s
        speed_mps = speed * 1000 / 3600

        time_cost = distance / speed_mps if speed_mps > 0 else distance

        congestion = random.uniform(0.5, 1.5)

        data["time"] = time_cost
        data["congestion"] = congestion

    return G


# ---------- DYNAMIC TRAFFIC UPDATE ----------

def update_traffic(G, peak=False):
    for u, v, data in G.edges(data=True):
        if peak:
            data["congestion"] = random.uniform(1.5, 3.0)
        else:
            data["congestion"] = random.uniform(0.5, 1.5)


# ---------- CUSTOM MULTI-FACTOR WEIGHT ----------

def multi_factor_weight(u, v, data, alpha=1.0, beta=1.0, gamma=1.0):
    d = data.get("length", 1)
    t = data.get("time", 1)
    c = data.get("congestion", 1)

    return alpha * d + beta * t + gamma * c


# ---------- ROUTING METHODS ----------

def run_routing(graph, source, target, mode="distance"):
    start = time.time()

    if mode == "distance":
        weight = "length"

    elif mode == "time":
        weight = "time"

    elif mode == "congestion":
        weight = "congestion"

    elif mode == "multi":
        weight = lambda u, v, d: multi_factor_weight(u, v, d)

    else:
        raise ValueError("Invalid mode")

    path = nx.shortest_path(graph, source=source, target=target, weight=weight)
    length = nx.path_weight(graph, path, weight="length")

    end = time.time()

    return {
        "mode": mode,
        "path": path,
        "length": length,
        "time": end - start,
        "nodes": len(path)
    }