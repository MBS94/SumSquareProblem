__author__ = 'Michael Byrd'
# Laptop

import time, random, math
from Graph import *
from MathFunctions import *
import csv
import ast
from SequenceFunctions import *

legalPaths = {}


def QRAdjList(n, p):  # Creates the Adjacency Matrix for Squares

    QRList = []

    for i in range(1, math.floor( (p-1)/2 ) + 1):
        qr = (i ** 2) % p
        if qr not in QRList:
            QRList.append(qr)

    QRList.sort()
    # print("QR", QRList, len(QRList))
    adjDict = {}
    for i in range(1, n + 1):
        adjDict[i] = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if ((i+j) % p) in QRList and i != j:
                adjDict[i].append(j)
    return adjDict



# print(QRAdjList(12, 13))

# g = Graph(QRAdjList(12, 29))

# print(len(g.findLongestPath(1, 2)))
for i in range(2, 31):
    for j in range(i + 1, i + 40):
        if is_prime(j):
            g = Graph(QRAdjList(i, j))
            if len(g.findLongestPath()) == i:
                print("P:", j, "Edge Count:", len(g.edges()))
                print("N:", i, g.findLongestPath())

# print(Graph(QRAdjList(12, 149)).edges())
