# finding a middle element in a linked list

"""

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

# lets use fast and slow pointer technique for finding the middle element
# Logic: once fast pointer reaches the end the slow pointer will be in middle
# odd length return middle
# evenlength return 2nd middle


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head: ListNode) -> ListNode:
    fastp = head
    slowp = head
    count = 1 # counter if count would be required

    while fastp and fastp.next:
        slowp = slowp.next
        count += 1
        fastp = fastp.next.next

    return slowp.val

