# Traversing the graph using Depth first search (DFS)

# visited set to keep track of visiting nodes
visited = set()

# using resursion
def dfs_recursion(visited, graph, node): # node is the starting node
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# DFS using stack
def dfs(visited, graph, node):
    stack = []
    stack.append(node)
    while stack:
        element = stack.pop()
        if element not in visited:
            print(element)
            visited.add(element)
            for neighbour in graph[element]:
                stack.append(neighbour)



# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

print(dfs(visited, graph, 'A'))