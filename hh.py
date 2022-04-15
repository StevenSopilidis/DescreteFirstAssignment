from operator import attrgetter
import random
import networkx as nx
import matplotlib.pyplot as plt

# function for checking if all elements of an sequence are zeros
# returns True if all elements of the sequence are zerors
def all_zeros(seq) -> bool:
    for i in range(len(seq)):
        if seq[i] != 0:
            return False
    return True

# function for drawing a sequence using havel-hakimi algorithm
# @param seq -> power sequence to draw
# returns true or false depending on wether we could draw it
def draw_sequence(seq) -> bool:
    if(nx.is_graphical(seq) == False):
        return False
    G = nx.Graph()
    V = [i for i in range(len(seq) - 1)]
    E = []

    # make a sequence that keeps track not only of the power of the sequence
    # but also which node it represents
    new_seq = [{"node": i, "power": seq[i]} for i in range(len(seq))]
    new_seq = sorted(new_seq, key=lambda node: node["power"], reverse=True)    
    
    for i in range(len(new_seq)):
        # select the random node
        node_index = random.randint(0, len(new_seq) - 1)
        node = new_seq[node_index]
        new_seq.pop(node_index)
        # add the neighbors
        for i in range(node["power"]):
            new_seq[i]["power"] -= 1
            E.append([new_seq[i]["node"], node["node"]])
        new_seq = sorted(new_seq, key=lambda node: node["power"], reverse=True)    
   
    #draw the graph
    G.add_nodes_from(V)
    G.add_edges_from(E)
    nx.draw(G)
    plt.show()
    return True

# seq1 = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]
# draw_sequence(seq1)
# seq2 = [6, 3, 3, 3, 3, 2, 2, 2, 2, 2,1,1]
# draw_sequence(seq2)