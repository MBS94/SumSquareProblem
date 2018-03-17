__author__ = 'Michael Byrd'

import time, random, math
from Graph import *
from MathFunctions import *
import csv
import ast
from SequenceFunctions import *


g = Graph(sumSquareList(1, 15))

print(g.vertices())

print(g.findLongestPath())
