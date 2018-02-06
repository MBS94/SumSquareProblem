__author__ = 'Michael Byrd'

# DFS Function from http://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming

import time
import random
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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.item)


class vertex(object):
    def __init__(self, k, adjacency):
        self.value = k
        self.adj = adjacency
        self.discover = False

    def discover(self):
        self.discover = True


def sumSquareList(m, n):  # Creates the Adjacency Matrix for Squares
    adjDict = {}
    for i in range(m, n + 1):
        adjDict[i] = []
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            if is_square(i + j) and i != j:
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


def dfs_iterative(graph, start):  # Non-recursive DFS I found Online, still working on learning how to write my own
    stack, path = [start], []

    while stack:
        # print(stack)
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
        print(path)
    return path


def legalSequence(seq):
    Flag = True

    for i in range(len(seq) - 1):
        if not is_square(seq[i] + seq[i + 1]):
            Flag = False
    return Flag

# r = 26
# for i in range(1, 90):
#     graph = Graph(sumSquareList(i, i + r))
#     for j in range(i, i + r):
#         for k in range(j, i + r):
#             if len(graph.findLongestPath(j, k)) == r + 1:
#                 print("(", i, ",", i+r, ") ", graph.findLongestPath(j, k), sep = '')
#             # else:
#             #     print("(", i, ",", i+r, ") BAD RANGE")


for n in range(25, 40):
    goodPaths = []

    graph = Graph(sumSquareList(1, n))
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            paths = graph.find_all_paths(i, j)
            for path in paths:
                if len(path) == n:
                    goodPaths.append(path)

    # for item in goodPaths:
    #     print(item)

    sumSequences = []

    for item in goodPaths:
        sumSeq = []
        for i in range(len(item) - 1):
            sumSeq.append(item[i] + item[i + 1])
        sumSequences.append(sumSeq)

    for item in sumSequences:
        print(sum(item))
    print("NEW LINE")