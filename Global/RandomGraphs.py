from igraph import Graph
import random
import networkx as nx


def generateCompleteEdgeList(size: int) -> list[tuple[int, int]]:
    """Generates list of tuples representing all possible edges of a simple graph.
    No loops are generated.

    Args:
        size (int): Number of vertices.

    Returns:
        list[tuple[int, int]]: List of possible edges.
    """
    return list(
        [(x, y) for x in range(size) for y in range(size) if x < y]
    )  # I'm sorry.


def randomGraphByEdges(size: int, edges: int) -> Graph:
    """Generates random undirected graph with specific number of edges.

    Args:
        size (int): Number of vertices.
        edges (int): Number of edges.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    return Graph(size, random.sample(generateCompleteEdgeList(size), edges))


def randomGraphByChance(size: int, probability: float) -> Graph:
    """Generates random undirected graph with specified probability for any edge to appear.

    Args:
        size (int): Number of vertices.
        probability (float): Probability for an edge to be created.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    edgeList = list(
        [e for e in generateCompleteEdgeList(size) if random.random() <= probability]
    )
    return Graph(size, edgeList)



def randomize_graph(graph: nx.Graph|Graph) -> nx.Graph:
    """
    Randomizes graph by removing random edge and connecting one of the vertices to random vertex.
    
    Args:
        graph (nx.Graph|Graph): Graph to randomize.
            
    Returns:
        nx.Graph: Randomized graph.
    """
    if isinstance(graph, Graph):
        graph = graph.to_networkx()

    try:
        edge_list = graph.edges()
        edge = random.choice(list(edge_list))
        graph.neighbors
        # mamy wiezrcholek z listy wierzcholkow bez wiierzcholkow polaczonych z pierwszym wierzvczolkiem wybranej krawedzi (nie moga byc polaczone)
        new_v = random.choice(list(set(graph.nodes()).difference(set([edge[0], *[n for n in graph.neighbors(edge[0])]]))))
        graph.remove_edge(*edge)
        graph.add_edge(edge[0], new_v)
        if graph:
            return graph
        else:
            return randomize_graph(graph)
    except:
        return randomize_graph(graph)
