__author__ = 'Michael Byrd'
# Laptop

import time, random, math
from Graph import *
from MathFunctions import *
import csv
import ast
from SequenceFunctions import *

legalPaths = {}

# for N in range(15, 25):
#     b = time.time()
#     g = Graph(sumSquareList(1, N))
#     legalPaths[N] = {}
#     for i in range(1, N + 1):
#         legalPaths[N][i] = []
#         for j in range(i, N + 1):
#             paths = g.find_all_paths(i, j)
#             for item in paths:
#                 if len(item) == N:
#                     legalPaths[N][i].append(item)
#     e = time.time()
#     print(N, e-b)
# writeList = []

# for key0 in legalPaths:
#     for key1 in legalPaths[key0]:
#         for item in legalPaths[key0][key1]:
#             # writeList.append(["N:", len(item), "\t (", item[0], ", ", item[-1], ") \t", item])
#             writeList.append([len(item), item[0], item[-1], item])
#             # print(len(item), "\t", item[0], "\t", item[-1], "\t", item)
#
# print(writeList[3])
#
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(writeList)

## GitHub




# for N in range(1, 31):
#     g = Graph(SquareSumDiffList(1, N))
#     for i in range(1, N + 1):
#         for j in range(i, N + 1):
#             if len(g.findLongestPath(i, j)) == N:
#                 print("N", N, "I", i, "J", j, g.findLongestPath(i, j), len(g.findLongestPath(i, j)))


# print(len(Graph(sumSquareList(1, 13)).edges()))

print(Graph(sumSquareList(1, 32)).findLongestPath())
