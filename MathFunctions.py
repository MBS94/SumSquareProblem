import math


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

def sumSquareList(m, n):  # Creates the Adjacency Matrix for Squares
    adjDict = {}
    for i in range(m, n + 1):
        adjDict[i] = []
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            if is_square(i + j) and i != j:
                adjDict[i].append(j)
    return adjDict

def SumDiffSquareList(m, n):
    adjDict = {}
    for i in range(m, n + 1):
        adjDict[i] = []
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            if is_square(i + j) and i != j:
                adjDict[i].append(j)
            if is_square(math.fabs(i - j)) and math.fabs(i - j) != 1 and i != j:
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