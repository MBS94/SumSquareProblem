import math
from Graph import *


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


def is_cube(integer):
    cubeRoot = round(math.pow(integer, (1 / 3)))
    if math.pow(cubeRoot, 3) == integer:
        return True
    else:
        return False


def sumSquareList(m, n):  # Creates the Adjacency List for Squares
    adjDict = {}
    for i in range(m, n + 1):
        adjDict[i] = []
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            if is_square(i + j) and i != j:
                adjDict[i].append(j)
    return adjDict


def SquareSumDiffList(m, n):
    adjDict = {}
    for i in range(m, n + 1):
        adjDict[i] = []
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            if is_square(i + j) and i != j:
                adjDict[i].append(j)
            if is_square(math.fabs(i - j)) and i != j and math.fabs(i-j) != 1:
                adjDict[i].append(j)
    return adjDict


def sumCubeList(k):  # Creates the Adjacency Matrix for Cubes
    adjDict = {}
    for i in range(1, k + 1):
        adjDict[i] = []
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if is_cube(i + j) and i != j:
                adjDict[i].append(j)
    return adjDict


def legalSequence(seq):
    Flag = True

    for i in range(len(seq) - 1):
        if not is_square(seq[i] + seq[i + 1]):
            Flag = False
    return Flag

# def pathFinder():
#     graph = Graph(sumSquareList(i, i + r))
#     for j in range(i, i + r):
#         for k in range(j, i + r):
#             if len(graph.findLongestPath(j, k)) == r + 1:
#                 print(r + 1, ", (", i, ",", i + r, ") ", graph.findLongestPath(j, k), sep='')
#             # else:
#             #     print("(", i, ",", i+r, ") BAD RANGE")
