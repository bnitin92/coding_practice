# Traversing the graph using Breadth first search (BFS)

visited = set()

def bfs(visited, graph, node):
    queue = []
    queue.append(node)

    while queue:
        element = queue.pop(0)
        if element not in visited:
            print(element)
            visited.add(element)
            for neighbour in graph[element]:
                queue.append(neighbour)

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

print(bfs(visited, graph, 'A'))


