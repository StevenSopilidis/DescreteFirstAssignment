import networkx as nx

# return a boolean indicating wether the graph contais an 
# eulerian graph
def printEulerTrail(n: int) -> bool:
    # create the complete graph
    g = nx.complete_graph(n)
    nodes = list(g.nodes())
    edges = list(g.edges())
    print(f"Node: {nodes}")
    print(f"Edges: {edges}")
    # check if there is an eulerian graph
    if(nx.has_eulerian_path(g) == False):
        return False

    return True


print(printEulerTrail(4))