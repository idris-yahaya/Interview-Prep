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