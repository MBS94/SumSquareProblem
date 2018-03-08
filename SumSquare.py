__author__ = 'Michael Byrd'
# Laptop

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



with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(writeList)

## GitHub
