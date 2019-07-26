'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

https://leetcode.com/problems/merge-two-sorted-lists/
'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def merge(A, B):
    dummy = Node(None)
    curr = dummy

    while A and B:
        if A.val < B.val:
            curr.next = A
            A = A.next
        else:
            curr.next = B
            B = B.next
        curr = curr.next

    if A and not B:
        curr.next = A
    elif B and not A:
        curr.next = B

    return dummy.next

A = None
B = Node(3, Node(6))

C = merge(A, B)

while C:
    print(C.val)
    C = C.next
