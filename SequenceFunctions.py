import time, random, math
from Graph import *
from MathFunctions import *
import csv

def sumSquare1toN(a, b):
    legalPaths = {}
    for N in range(a, b):
        b = time.time()
        g = Graph(sumSquareList(1, N))
        legalPaths[N] = {}
        for i in range(1, N + 1):
            legalPaths[N][i] = []
            for j in range(i, N + 1):
                paths = g.find_all_paths(i, j)
                for item in paths:
                    if len(item) == N:
                        legalPaths[N][i].append(item)
        e = time.time()
        print(N, e - b)
    writeList = []
    for key0 in legalPaths:
        for key1 in legalPaths[key0]:
            for item in legalPaths[key0][key1]:
                # writeList.append(["N:", len(item), "\t (", item[0], ", ", item[-1], ") \t", item])
                writeList.append([len(item), item[0], item[-1], item])
                # print(len(item), "\t", item[0], "\t", item[-1], "\t", item)
    with open("SquareSumOutput.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(writeList)


def LegalSeqSumDiff(a, b):
    legalPaths = {}
    for N in range(a, b):
        bTime = time.time()
        g = Graph(SquareSumDiffList(1, N))
        legalPaths[N] = {}
        for i in range(1, N + 1):
            legalPaths[N][i] = []
            for j in range(i, N + 1):
                paths = g.find_all_paths(i, j)
                for item in paths:
                    if len(item) == N:
                        legalPaths[N][i].append(item)
        eTime = time.time()
        print(N, eTime - bTime)
    for key0 in legalPaths:
        for key1 in legalPaths[key0]:
            for item in legalPaths[key0][key1]:
                # writeList.append(["N:", len(item), "\t (", item[0], ", ", item[-1], ") \t", item])
                # writeList.append([len(item), item[0], item[-1], item])
                print(len(item), "\t", item[0], "\t", item[-1], "\t", item)


def sumSquareMtoN(a, b, k):
    legalPaths = []
    for M in range(0, k):
        for N in range(a+M, b+M):
            bTime = time.time()
            g = Graph(sumSquareList(a+M, N))
            for i in range(a+M, N + 1):
                for j in range(i, N + 1):
                    paths = g.find_all_paths(i, j)
                    for item in paths:
                        if len(item) == N:
                            legalPaths.append(item)
            eTime = time.time()
            print(a+M, N, eTime - bTime)
    for item in legalPaths:
        print(min(item), max(item), item)