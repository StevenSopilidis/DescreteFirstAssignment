import networkx as nx
import random

def TSort(G: nx.DiGraph) -> list:
    # copy G so we dont mess original graph
    copy = G.copy()
    sort = []
    # # while we have nodes remaining
    while(len(copy) > 0):
        # find an zero input node and remove it
        for v in copy.nodes():
            if(copy.in_degree(v) == 0):
                sort.append(v)
                copy.remove_node(v)
                break
    return sort

G1 = nx.DiGraph()
V = [i for i in range(1,10)]
U = [[1,8],[6,1],[6,8],[7,5],[4,1],[4,9],[2,6],[2,9],[3,8],[9,8],[8,5],[8,7]]

# for having different sort just suffle the array of nodes before creating 
# graph

# first sort
G1.add_nodes_from(V)
G1.add_edges_from(U)
sort1 = TSort(G1)
# second sort
G2 = nx.DiGraph()
random.shuffle(V)
G2.add_nodes_from(V)
G2.add_edges_from(U)
sort2 = TSort(G2)
# third sort
G3 = nx.DiGraph()
random.shuffle(V)
G3.add_nodes_from(V)
G3.add_edges_from(U)
sort3 = TSort(G3)

# print the sorts
print(f"Sort1: {sort1}\nSort2: {sort2}\nSort3: {sort3}")