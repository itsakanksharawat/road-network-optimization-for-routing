import matplotlib.pyplot as plt
import networkx as nx


def get_pos(G):
    return {node: (data['x'], data['y']) for node, data in G.nodes(data=True)}


def plot_graph(G, title="Graph"):
    plt.figure(figsize=(8, 8))
    pos = get_pos(G)

    nx.draw(G, pos, node_size=5, edge_color="gray")

    plt.title(title)
    plt.show()


def plot_graph_with_path(G, path, title="Path Visualization"):
    plt.figure(figsize=(8, 8))
    pos = get_pos(G)

    nx.draw(G, pos, node_size=5, edge_color="lightgray")

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    plt.title(title)
    plt.show()