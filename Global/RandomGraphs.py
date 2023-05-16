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
        [e for e in generateCompleteEdgeList(
            size) if random.random() <= probability]
    )
    return Graph(size, edgeList)


def randomize_graph(graph: nx.Graph | Graph) -> nx.Graph:
    """
    Randomizes graph by removing random edge and connecting one of the vertices to random vertex.

    Args:
        graph (nx.Graph|Graph): Graph to randomize.

    Returns:
        nx.Graph: Randomized graph.
    """
    if isinstance(graph, Graph):
        graph = graph.to_networkx()


    edge_list = graph.edges()
    edge1 = random.choice(list(edge_list))
    edge2 = random.choice(list(edge_list))
    if len(set([edge1[0], edge1[1], edge2[0], edge2[1]])) != 4:
        return randomize_graph(graph)
    graph.remove_edge(*edge1)
    graph.remove_edge(*edge2)

    # check if edge already exists
    if graph.has_edge(edge1[0], edge2[1]) or graph.has_edge(edge2[0], edge1[1]):
        return randomize_graph(graph)

    graph.add_edge(edge1[0], edge2[1])
    graph.add_edge(edge2[0], edge1[1])

    return graph
    
