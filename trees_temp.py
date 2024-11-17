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

def in_order_list(node):
    if not node:
        return []

    # Combine left, middle, and right into a list
    return in_order_list(node.left) + [node.data] + in_order_list(node.right)

def search_while(node, target):
    curr_node = node

    while curr_node:
        if target == curr_node.data:
            return node
        
        if target < curr_node.data:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
    return None

def search_rec(node, target):
    if not node:
        return None
    
    if node.data == target:
        return node
    
    if target < node.data:
        return search_rec(node.left, target)
    else:
        return search_rec(node.right, target)
    
# Better Implement this
def insert_rec(node, data):
    # Base Case: When leaf has no next (left/right)
    if data < node.data:
        # Case 1: Child Node
        if node.left:
            insert_rec(node.left, data)
        else:
            # Case 2: Null Node
            node.left = TreeNode(data)
    else:
        # Case 1: Child Node
        if node.right:
            insert_rec(node.right, data)
        else:
            # Case 2: Null Node
            node.right = TreeNode(data)

def insert(node, data):
    if not node:
        return TreeNode(data)
    elif data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node

def min_value_node(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr

# def delete(node, data):

#     # Base Case: Reached EO Tree
#     if not node:
#         return None
#     elif data == node.data:         # Value Found
        
#         if not (node.left or node.right):   # Case 1: 0 Child Nodes
#             return None
#         elif (node.left and node.right):    # Case 3: 2 Child Nodes
#             # Retrieve in order successor (min value on nodes right subtree)
#             swap_node = min_value_node(node.right)

#             # What if min value has a right child?
#             # Delete Old in order successor
#             node.right = delete(node.right, swap_node.data)
#             node.data = swap_node.data
#         else:                               # Case 2: 1 Child Nodes
#             node = node.left if node.left else node.right
#     elif data < node.data:
#         node.left = delete(node.left, data)     # Search Left
#     elif data > node.data:
#         node.right = delete(node.right, data)    # Search Right
    
#     return node

def delete(node, data):
    if not node:
        return None
    
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:

        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        
        node.data = min_value_node(node.right).data
        node.right = delete(node.right, node.data)
    
    return node




# Min Node
# Delete
# BFS / DFS

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
in_order(root)

print(in_order_list(root))

print(search_while(root, 30))
print(search_rec(root, 18))

# insert_rec(root, 19)
# print(in_order_list(root))


test = insert(root, 19)
test = insert(root, 12)
test = insert(root, 19)

print(in_order_list(test))



print(in_order_list(min_value_node(node7)))

delete(root, 3)
print(in_order_list(root))

delete(root, 3)
print(in_order_list(root))

delete(root, 13)
print(in_order_list(root))


# BST Complexity:
# Operation    Time Complexity (Best - Balanced)       Time Complexity (Worst - Unbalanced)     Space Complexity
# Search       O(log n)                     O(h)                        O(h)
# Insert       O(log n)                     O(h)                        O(h)
# Delete       O(log n)                     O(h)                        O(h)