from .DataTypes import *
from .RandomGraphs import *

if __name__ == "__main__":

    graphAL = random_graph_by_edges(9,10)

    graphAL.data = [[4,6,7],[],[5,7],[4,5],[0,3,5,8],[2,3,4],[0,8],[0,2],[4,6]]
    graphAM = graphAL.to_adjacency_matrix()
    graphIM = graphAL.to_incidence_matrix()
    print(graphAL)  # default
    print(graphAM)  # AL - AM
    print(graphIM)  # AM - IM
    print(graphIM.to_adjacency_matrix())  # IM - AM
    print(graphAM.to_adjacency_list())  # AM - AL
    print(graphIM.to_adjacency_list())  # IM - AL
    print(graphAL.to_incidence_matrix().to_adjacency_matrix())  # AL - IM - AL
