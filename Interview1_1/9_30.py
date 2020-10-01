# finding the depth of a binary tree

"""
input : root
Binary tree : not balanced

ouput: the height of the tree

                    5
                /    \
                4     7
            /    \     \
           12    15      15
                            \
                            19
use Breadth first search
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def height(root):
    # BFS use queues

    #res = []

    if root == None:
        return None

    queue = []

    queue.append(root)

    count = -1

    while queue:
        level_length = len(queue)
        levelelement = []
        count += 1
        for _ in range(level_length):
            current = queue.pop(0)
            levelelement.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        #res.append(levelelement)

    return count #len(res) - 1

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(5)

    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(7)
    # root.left.left = TreeNode(12)
    # root.left.right = TreeNode(15)

    #root = TreeNode(5)

    #root = None

    print("height:", str(height(root)))

main()