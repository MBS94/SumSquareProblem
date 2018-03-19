__author__ = 'Michael Byrd'
# Laptop

import time, random, math
from Graph import *
from MathFunctions import *
import csv
import ast
from SequenceFunctions import *

legalPaths = {}


def QRList(p):
    QRList = []
    for i in range(1, math.floor( (p-1)/2 ) + 1):
        qr = (i ** 2) % p
        if qr not in QRList:
            QRList.append(qr)
    QRList.sort()
    return QRList



def QRAdjList(n, p):  # Creates the Adjacency Matrix for Squares
    qrList = QRList(p)
    adjDict = {}
    for i in range(1, n + 1):
        adjDict[i] = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if ((i+j) % p) in qrList and i != j:
                adjDict[i].append(j)
    return adjDict

def min_prime_dirac(n):
    flag = True
    p = n + 1
    while flag:
        if is_prime(p):
            qrList = QRList(p)
            adjList = QRAdjList(n, p)

            flag1 = True
            for key in adjList:
                # print(key)
                # print(p, len(adjList[key]))
                if len(adjList[key]) < (n / 2):
                    flag1 = False
            if flag1:
                return p
            # print("P:", p)
        p += 1


print(Graph(QRAdjList(8, 37)).edges())

# for N in range(5, 51):
#     for p in range(N + 1, 400):
#         if is_prime(p):
#             x = (QRAdjList(N, p))
#             # print("Prime:", p)
#             flag = True
#             for k in x:
#                 if len(x[k]) < N/2:
#                     flag = False
#             if flag:
#                 print("N", N, "Prime:", p)

b = time.time()
for N in range(3, 150):
    print("N:", N, "Prime:", min_prime_dirac(N))
    min_prime_dirac(N)
e = time.time()

print(e-b)
