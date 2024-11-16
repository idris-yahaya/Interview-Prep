""" Stacks """
# Time Complexity
# Push: O(1), Pop: O(1), Peek: O(1)

# Creating and pushing elements onto the stack
stack = []
stack.append(10)  # Adds 10
stack.append(20)  # Adds 20

# Popping elements from the stack
last_item = stack.pop()  # Removes and returns 20

# Peeking at the top element
top_item = stack[-1] if stack else None  # Returns 10 (top of the stack)

# Checking if the stack is empty
is_empty = len(stack) == 0





""" Stacks """

# Quick Implementation --------

# Declaration
stack = []

# Push
stack.append(5)

# Pop
pop_top = stack.pop() if stack else None

# Peek
top_item = stack[-1] if stack else None

# Is Empty

is_empty = not stack

# Class Implementation --------

class Stack:
    def __init__(self):
        self.items = []
    
    # Push
    def push(self, value):
        self.items.append(value)

    # Pop
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    # Peek
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # Is Empty
    def is_empty(self):
        return not self.items


# Test the stack
stack = Stack()
assert stack.is_empty() == True, "Stack should be empty initially"

stack.push(5)
assert stack.is_empty() == False, "Stack should not be empty after a push"
assert stack.peek() == 5, "Top of the stack should be 5"

stack.pop()
assert stack.is_empty() == True, "Stack should be empty after popping the last element"


""" Queues """

# Quick Implementation --------
from collections import deque

# Declaration
queue = deque()

# Enqueue
queue.append(5)

# Dequeue
dequeue_top = queue.popleft() if queue else None

# Peek
peek_top = queue[0] if queue else None

# Is Empty
is_empty = not queue


# Class Implementation --------

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def peek(self):
        if self.items:
            return self.items[0]
        return None
    
    def is_empty(self):
        return not self.items