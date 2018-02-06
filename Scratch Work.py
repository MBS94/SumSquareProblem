# num = 300
#
# adjacency_matrix = sumSquareList(num)
#
# adjList = []
#
# for key in adjacency_matrix:
#     adjList.append(adjacency_matrix)
#
# graph = Graph(adjacency_matrix)

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

# adjacency_matrix = sumSquareList(15)
# g = Graph(adjacency_matrix)
# p = g.find_all_paths(8, 9)
# for item in p:
#     print(item)

# k = 15
# for i in range(15, 30):
#     adjacency_matrix = sumSquareList(i)
#     graph = Graph(adjacency_matrix)
#     legalPaths = []
#     for j in range(1, i + 1):
#         for k in range(1, i + 1):
#             # print(j, k)
#             paths = graph.find_all_paths(j, k)
#             for item in paths:
#                 if len(item) == i:
#                     print(item)
#     blank = input()


# for k in range(1, 200):
#     adjMatrix = sumCubeList(k)
#     # print(adjMatrix)
#     g = Graph(adjMatrix)
#     longestPath = []
#     for i in range(1, k):
#         for j in range(i, k):
#             paths = g.find_all_paths(i, j)
#             for item in paths:
#                 if len(item) >= len(longestPath):
#                     longestPath = item
#     print(longestPath, "K", k, "Length", len(longestPath))



# for i in range(len(sumSequences[0])):
#     if sumSequences[0][i] == sumSequences[1][i] and\
#             sumSequences[1][i] == sumSequences[2][i] and\
#             sumSequences[0][i] == sumSequences[2][i]:
#         pass
#     else:
#         sumSequences[0][i], sumSequences[1][i], sumSequences[2][i] = "X", "X", "X"
#
# for item in sumSequences:
#     print(item)

