
# 18. Linked List
"""
Linked lists are made up of nodes, where each node contains a reference to the next node in the list.
In addition, each node contains a unit of data called the CARGO.
A linked list is considered a Recursive Data Structure because it has a recursive definition.

Single Linked List & Double Linked List
-- Size: Grow and contract since of insertions and deletions. Maximum size depends on heap.
-- Storage Capacity: Dynamic (it's node is located during run time)
-- Order and Sorting: Stored randomly
-- Accessing the Elements: Sequential access method. Traverse starting fro the first node in the list by pointer.
-- Searching: Linear search
"""


# 18.1 "Node" class
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

node = Node("test")
print(node)

# create a list with more than one mode
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

