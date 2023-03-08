from DataTypes import *
from RandomGraphs import *

if __name__ == "__main__":

    graphAL = randomGraphByEdges(10, 12)
    graphAM = AL_to_AM(graphAL)
    graphIM = AM_to_IM(graphAM)
    print(graphAL)  # default
    print(graphAM)  # AL - AM
    print(graphIM)  # AM - IM
    print(IM_to_AM(graphIM))  # IM - AM
    print(AM_to_AL(graphAM))  # AM - AL
    print(IM_to_AL(graphIM))  # IM - AL
    print(IM_to_AL(AL_to_IM(graphAL)))  # AL - IM
