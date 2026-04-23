import networkx as nx

def remove_micro_edges(G, threshold=2):
    edges_to_remove = []

    for u, v, data in G.edges(data=True):
        length = data.get("length", 0)

        # Keep critical edges
        if length > 0 and length < threshold:
            edges_to_remove.append((u, v))

    G.remove_edges_from(edges_to_remove)
    return G


def remove_degree2_nodes(G):
    nodes_to_remove = []

    for node in list(G.nodes()):
        if G.degree(node) == 2:
            neighbors = list(G.neighbors(node))

            if len(neighbors) == 2:
                u, v = neighbors

                # Avoid duplicate edges
                if G.has_edge(u, v):
                    continue

                length_u = G[node][u].get("length", 0)
                length_v = G[node][v].get("length", 0)

                G.add_edge(u, v, length=length_u + length_v)
                nodes_to_remove.append(node)

    G.remove_nodes_from(nodes_to_remove)
    return G


def clean_graph(G):
    G = remove_micro_edges(G, threshold=2)
    G = remove_degree2_nodes(G)
    return G