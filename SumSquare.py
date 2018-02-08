__author__ = 'Michael Byrd'

import time, random, math
from Graph import *
from MathFunctions import *

for r in range(22, 35):
    for i in range(1, 150):
        graph = Graph(sumSquareList(i, i + r))
        for j in range(i, i + r):
            for k in range(j, i + r):
                if len(graph.findLongestPath(j, k)) == r + 1:
                    print(r + 1, ", (", i, ",", i + r, ") ", graph.findLongestPath(j, k), sep='')
                # else:
                #     print("(", i, ",", i+r, ") BAD RANGE")

# for n in range(25, 30):
#     goodPaths = []
#
#     graph = Graph(sumSquareList(1, n))
#     for i in range(1, n + 1):
#         for j in range(i, n + 1):
#             paths = graph.find_all_paths(i, j)
#             for path in paths:
#                 if len(path) == n:
#                     goodPaths.append(path)
#
#     for item in goodPaths:
#         print(item)
#
#     sumSequences = []
#
#     for item in goodPaths:
#         sumSeq = []
#         for i in range(len(item) - 1):
#             sumSeq.append(item[i] + item[i + 1])
#         sumSequences.append(sumSeq)

# for item in sumSequences:
#     print(sum(item))
# print("NEW LINE")
