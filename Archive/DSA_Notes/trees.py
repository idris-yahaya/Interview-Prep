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

# Inorder (LNR): Left → Node → Right.
# Preorder (NLR): Node → Left → Right.
# Postorder (LRN): Left → Right → Node.
# Level Order (BFS): Visit nodes level by level (use a queue).
# Depth-First Search (DFS): Explore each branch fully before moving to the next.
# Breadth-First Search (BFS): Explore all nodes at the present depth before moving to the next.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):
    if not node:
        return
    
    # Recurse Left
    in_order(node.left)

    # Print Middle
    print(node.data)

    # Recurse Right
    in_order(node.right)


root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)