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


def sumSquareList(k):  # Creates the Adjacency Matrix
    adjDict = {}
    for i in range(1, k + 1):
        adjDict[i] = []
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if is_square(i + j) and i != j:
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


num = 300

adjacency_matrix = sumSquareList(num)

adjList = []

for key in adjacency_matrix:
    adjList.append(adjacency_matrix)

graph = Graph(adjacency_matrix)

# print(graph)


# print(len(adjList))

# for k in range(1, num + 1):  # To check if the Path is valid, checks every possible start
#     flag = True
#     path = (dfs_iterative(adjacency_matrix, k))
#     for i in range(len(path) - 1):
#         if not is_square(path[i] + path[i + 1]):
#             flag = False
#     # print(k, path)
#     if flag:
#         print(k)

# path18 = (dfs(adjList, 18))

# print(path18)
#
# for i in range(len(path18) - 1):
#     print(path18[i], path18[i + 1], "SUM", path18[i] + path18[i + 1] )

# for k in range(25, 301):
#     s = time.time()
#     i = int(((math.floor(math.sqrt(k)) + 1) ** 2) / 2)
#     j = random.randint(i, k)
#     adjacency_matrix = sumSquareList(k)
#     graph = Graph(adjacency_matrix)
#     foundPath = False
#     while i <= k and not foundPath:
#         j = random.randint(i, k)
#         while j <= k and not foundPath:
#             # print(i, j, k)
#             paths = (graph.find_all_paths(i, j))
#             for item in paths:
#                 if legalSequence(item) and len(item) == k:
#                     # print("LEGAL", item)
#                     foundPath = True
#                     goodPath = item
#             j += 1
#         i += 1
#     e = time.time()
#     print(k, e - s, goodPath)


# adjacency_matrix = sumSquareList(45)
# for key in adjacency_matrix:
#     print(key, adjacency_matrix[key])
# graph = Graph(adjacency_matrix)
#
# list = graph.findCompletePath(18, 32, 45)
#
# print(graph)

k = 15
for i in range(15, 30):
    adjacency_matrix = sumSquareList(i)
    graph = Graph(adjacency_matrix)
    legalPaths = []
    for j in range(1, i + 1):
        for k in range(1, i + 1):
            # print(j, k)
            paths = graph.find_all_paths(j, k)
            for item in paths:
                if len(item) == i:
                    print(item)
    blank = input()
# adjacency_matrix = sumSquareList(15)
# g = Graph(adjacency_matrix)
# p = g.find_all_paths(8, 9)
# for item in p:
#     print(item)