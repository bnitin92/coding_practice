# find all paths from source to target

"""
Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1,
and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

"""

# not necessary to do
# convert graph from list of list to dict
def list_to_dict(l):
    return dict(zip([i for i in range(len(l))], l))


def bfs(graph, node):
    visited = set()
    path = []
    queue = []
    queue.append(node)
    while queue:
        element = queue.pop(0)
        if element not in visited:
            visited.add(element)
            path.append(element)
            for neighbour in graph[element]:
                queue.append(neighbour)

    return path

# write code but wrong logic

# def allPathsSourceTarget(graph):
#     #graph = list_to_dict(graph)
#     res = []
#
#     for node in graph[0]:
#         path = bfs(graph, node)
#         if len(graph)-1 in path:
#             path.insert(0,0)
#             res.append(path)
#
#     return res


# Count by dfs with memo.
def allPathsSourceTarget(graph):
    def dfs(curr, path):
        if curr == len(graph) - 1:
            res.append(path)
        else:
            for i in graph[curr]:
                dfs(i, path + [i])

    res = []
    dfs(0, [0])

    return res


#graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]] # this gives the wrong answer for the previous one
# print(graph)
# print(bfs(graph, 0))
print(allPathsSourceTarget(graph))



#print(list_to_dict(graph))

#print([i for i in len(graph)])