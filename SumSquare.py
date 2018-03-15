__author__ = 'Michael Byrd'


import time, random, math
from Graph import *
from MathFunctions import *
import csv
import ast
from SequenceFunctions import *

sequenceList = []

f = open('15-39.csv', 'r')
reader = csv.reader(f)
for row in reader:
    sequenceList.append((row[3]))
f.close()



# for i in range(30):
#     sequenceList[i] = ast.literal_eval(sequenceList[i])
#     if len(sequenceList[i]) % 2 == 0:
#         for j in range(0, len(sequenceList[i]), 2):
#             print(sequenceList[i][j] + sequenceList[i][j+1])


g = Graph(sumSquareList(1, 15))

paths = g.find_all_paths()