# Binary Tree Level Order Traversal

"""
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

"""

# class Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def BFS(root):
    result = []

    if root == None:
        return None

    queue = []
    queue.append(root)

    while queue:
        levelsize = len(queue)
        currentlevel = []

        for _ in range(levelsize):
            curr = queue.pop(0)
            currentlevel.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        result.append(currentlevel)

    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: ", str(BFS(root)))

main()
