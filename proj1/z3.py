from DataTypes import *
from Methods import *

if __name__ == "__main__":

    graph = randomGraphByEdges(10, 12)

    print(graph)

    graph2 = randomGraphByChance(10, 0.5)

    print(graph2)
