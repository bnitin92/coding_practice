# I have to find whether i am able to reach all the doors starting from zero

"""

Input: [[1],[2],[3],[]]

Output: boolean (T/F)

"""

"""
My approach
apply DFS to the solution 
 create a list remaining  = from [1..len(graph)-1]
 
 indicator while all the nodes are traversed and remaining 
if neighbour in remaing: 
    remainig.remove(neighbour)

return len(remaining) == 0

"""

# Runtime = O(V+E)
#def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
def canVisitAllRooms(rooms):
    rem_rooms = [i for i in range(1, len(rooms))]

    visited = set()
    def dfs(r, key):
        stack = [key]

        while stack and rem_rooms:
            element = stack.pop()
            if element in rem_rooms:
                rem_rooms.remove(element)

            if element not in visited:
                visited.add(element)

                for neighbour in rooms[element]:
                    stack.append(neighbour)

    dfs(rooms, 0)

    return len(rem_rooms) == 0


#rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms))
