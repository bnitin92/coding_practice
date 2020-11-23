# from sam
# reverse a LL

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printreverseLL(head):
    if head == None:
        return
    printreverseLL(head.next)
    print(head.val)

#Creating a linked list
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

print(printreverseLL(head))
