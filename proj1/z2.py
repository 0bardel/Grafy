import Visualization
from RandomGraphs import random_graph_by_chance

if __name__ == "__main__":
    graph = random_graph_by_chance(7, 0.7)
    Visualization.draw_graph(graph)