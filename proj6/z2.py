import matplotlib.pyplot as plt
import numpy as np

with open('input_150.dat') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split() for line in lines]
    lines = [[float(x) for x in line] for line in lines]
    lines = *zip(*lines),
    plt.figure()
    plt.plot(lines[0], lines[1])
    plt.show()

with open('z2.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split() for line in lines]
    lines = [[float(x) for x in line] for line in lines]
    lines = *zip(*lines),
    plt.figure()
    plt.plot(lines[0], lines[1])
    plt.show()
