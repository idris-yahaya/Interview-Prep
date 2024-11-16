# Node Class

# class Node:
#     def __init__(self, value=0, right=None, left=None):
#         self.value = value
#         self.right = right
#         self.left = left

# BST Class
class Node:
    def __init__(self, value=0, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left
    
    
    # Insertion
    def insert(self, value):
        if (value < self.value):
            if (self.left):
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if (self.right):
                self.right.insert(value)
            else:
                self.right = Node(value)

    # Search

    # Traversal
    def inorder(self):
        # Left, Root, Right
        if self.left:
            self.left.inorder()
        
        print(self.value)

        if self.right:
            self.right.inorder()


if __name__ == "__main__":
    my_bst = Node(20)
    my_bst.inorder()
    my_bst.insert(10)
    my_bst.insert(15)
    my_bst.insert(5)
    my_bst.insert(35)
    my_bst.inorder()



# Tree Terminology
# Whole Tree, Root, Edges, Nodes, Leaf Nodes, Child Nodes, Parent/Internal Nodes, Tree Height, Tree Size


# Tree Types
# Binary
# Each Node has 0-2 children (left, right)
# Binary Search Trees (BSTs)
# Left child has lower value, right side has higher
# AVL Trees
# Self balancing BST, height difference between left/right sub trees is at most 1 (dont through rotations when inserting or deleting)

# Tree Variants (Balanced, Complete, Full, Perfect)
# Balanced: Max 1 diff between left/right subtree heights, for each node
# Complete: All levels except leaves must be filled (inherently balanced)
# Full: Each node has 0 or 2 child nodes
# Perfect: All leaves on same level, All internal nodes have two children - Full, Balanced, Complete


# Binary Tree Traversals

# Breadth First Search (BFS)
# Visit all nodes at the current level before moving to the next level

# Depth First Search (DFS)
# Visit all nodes along a path (branch) as far as possible before backtracking

# 1. Pre-order Traversal (Node → Left → Right)

# 2. In-order Traversal (Left → Node → Right)
# 3. Post-order Traversal (Left → Right → Node)
