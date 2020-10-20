# Scheduling the task

"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need
to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs,
find out if it is possible to schedule all the tasks.
"""

"""
topological sorting where i will sort the vertices based on given relations and find out if task scheduling is 
possible or not

"""

from collections import deque

def scheduling(tasks, prerequisites):

    scheduleOrder = []

    if tasks <= 0:
        return scheduleOrder

    # initialize the graph
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # populate the graph and indegree
    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        inDegree[child] += 1
        graph[parent].append(child)

    # from where the things originate
    sources = deque()
    for node in inDegree:
        if inDegree[node] == 0:
            sources.append(node)

    while sources:
        vertex = sources.popleft()
        scheduleOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # check for cycles
    # if len(scheduleOrder) > tasks:
    #     return False
    print(graph)
    print(scheduleOrder)
    return len(scheduleOrder) == tasks


def main():
    print(scheduling(3, [[0, 1], [1, 2]]))
    print(scheduling(3, [[0, 1], [1, 2], [2, 0]])) # none will have indgree one
    print(scheduling(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
main()
