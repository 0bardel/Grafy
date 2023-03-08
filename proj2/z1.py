from igraph import Graph
import numpy as np
from Global.GraphicSequence import *
from Global.RandomGraphs import *

if __name__ == "__main__":
    sequence1 = [6, 4, 2, 2, 2, 1, 1]
    sequence2 = [6, 2, 5, 6, 1, 3]
    sequence3 = [4, 0, 0, 0, 0]

    print(f"{sequence1} -> {isSequenceGraphic(sequence1)}")
    print(f"{sequence2} -> {isSequenceGraphic(sequence2)}")
    print(f"{sequence3} -> {isSequenceGraphic(sequence3)}")

    graph = graphFromSequence([6, 4, 2, 2, 2, 1, 1])
    print(graph.to_tuple_list())
    print(graph.get_adjlist())
