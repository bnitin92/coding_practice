# Finding topological sort of a given graph

"""
Whenever find a graph problem where we are required an ordering of vertices we perform topological sort

1. Should be a DAG(that is no cycles)
2. can use breadth first search to traverse the graph to traverse all the nodes

"""

from collections import deque

def topological_sort(vertices, edges):
    sortedOrder = []

    # edge case if no vertices
    if vertices <= 0:
        return sortedOrder

    # a. initialize graph
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # b. build graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1

    # c. find all sources wiht indegree 0
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. each source add in sorted order and decrement the child
    while sources:
        node = sources.popleft()
        sortedOrder.append(node)
        for child in graph[node]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # if there is a cycle
    if len(sortedOrder) > vertices:
        return []

    return sortedOrder

def main():
    print("Topological sort: " + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " + str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()