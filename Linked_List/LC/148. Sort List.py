# sort a linked list

"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# normal method
"""
convert the linkedlist to array and then sort and return it
"""
def sortList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next

    result.sort()
    # print(result, resultll)
    resultll = curr = ListNode()

    for i in result:
        curr.next = ListNode(val=i)
        curr = curr.next

    return resultll.next

# In place list sorting method
"""
Apply 2 methods first divide into halves and merge the 2 linked lists
"""

def sortList(head):

    def mergelist(l1, l2):
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2

        return dummy.next

    def middleval(head):
        fastp = slowp = head

        while fastp.next and fastp:
            fastp = fastp.next.next
            slowp = slowp.next

        return slowp.val










# Creating a linked list
# head = Node(2)
# head.next = Node(4)
# head.next.next = Node(6)
# head.next.next.next = Node(8)
# head.next.next.next.next = Node(10)