import networkx as nx

def preprocess_graph(G):
    # Convert to undirected
    G = nx.Graph(G)

    # Remove isolated nodes
    G.remove_nodes_from(list(nx.isolates(G)))

    return G