# not solve, it is backtracking

"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks
which need to be completed before it can be scheduled. Given the number of tasks and a list
of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

"""

"""
So I can do topological sort and find out if it is possible to get all the sequences. 
so the sequences will be depending upon the number of sources in 

"""

from collections import deque

def print_orders(tasks, prerequisites):
    orders = []

    # if no orders
    if tasks <= 0:
        return orders

    # make the graph and inDegree
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        inDegree[child] += 1
        graph[parent].append(child)

    sources = deque()

    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        node = sources.popleft()
        orders.append(node)

        for vertex in graph[node]:
            inDegree[vertex] -= 1
            if inDegree[vertex] == 0:
                sources.append(vertex)


    if len(orders) != tasks:
        return []

    return orders

def main():
    print("print order:" + str(print_orders(3, [[0, 1], [1, 2]])))
    print("print order:" + str(print_orders(3, [[0, 1], [1, 2], [2, 0]]))) # none will have indgree one
    print("print order:" + str(print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()