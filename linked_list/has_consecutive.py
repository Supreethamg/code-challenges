# Write a function that takes in the head of a singly-linked list. It should return True if two nodes with the same data appear consecutively.

# Example test cases:

# in: 1 → 2 → 2
# out: True

# in: 1 → 2 → 1
# out: False

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def has_consecutive(self):
        data = None
        current= self.head
        