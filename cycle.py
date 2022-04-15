import matplotlib.pyplot as plt
import networkx as nx
from numpy import void

def draw_cycle(nodes: int) -> void:
    G = nx.Graph()
    V = [i for i in range(0,nodes)]
    E = []

    # connect each node with its next starting from node 1
    for i in range(nodes - 1):
        E.append([i,i+1])
    E.append([nodes - 1, 0])
    
    G.add_nodes_from(V)
    G.add_edges_from(E)
    nx.draw_circular(G)
    plt.show()


draw_cycle(20)