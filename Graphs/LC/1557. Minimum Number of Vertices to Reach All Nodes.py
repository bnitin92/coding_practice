# Find the minimum number of vertices to reach all nodes

"""

inshort we need to find edges without any incomming nodes

"""

# gives time exceed
#def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
# def findSmallestSetOfVertices(n, edges):
#
#     vertices = [i for i in range(n)]
#
#     for i in edges:
#         if i[1] in vertices:
#             vertices.remove(i[1])
#
#     return vertices


def findSmallestSetOfVertices(n, edges):
    return list(set(range(n)) - set(j for i, j in edges))


print(findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))
