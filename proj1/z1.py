from DataTypes import *
from Methods import *

if __name__ == "__main__":

    graphAL = random_graph_by_edges(10, 12)
    graphAM = graphAL.to_adjacency_matrix()
    graphIM = graphAL.to_incidence_matrix()
    print(graphAL)  # default
    print(graphAM)  # AL - AM
    print(graphIM)  # AM - IM
    print(graphIM.to_adjacency_matrix())  # IM - AM
    print(graphAM.to_adjacency_list())  # AM - AL
    print(graphIM.to_adjacency_list())  # IM - AL
    print(graphAL.to_incidence_matrix().to_adjacency_matrix())  # AL - IM - AL
