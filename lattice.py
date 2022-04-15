import matplotlib.pyplot as plt
import networkx as nx

# @param n: number of rows in lattice
# @param m: number of cols in lattice
def draw_lattice(n: int,m: int) -> None:
    G = nx.Graph()
    V = [i for i in range(n * m)]
    E = []

    # connect the rows
    for i in range(0, n * m - 1):
        if((i + 1) % m == 0 and i != 0):
            pass
        else:
            E.append([i, i + 1])

    # connect the cols
    for i in range(0, n * m - m):
        E.append([i, i + m])
    
    G.add_nodes_from(V)
    G.add_edges_from(E)
    nx.draw(G)
    plt.show()

draw_lattice(5,5)
