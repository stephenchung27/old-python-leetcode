'''
You are given a complete binary tree numbered from left to right.
Return if the nth node exists in the tree.

Follow up:
Return the number of nodes in the tree in better than linear time.

A perfect binary tree has 2 ** height - 1 number of nodes.
A complete binary tree is a balanced binary tree with all its interior nodes
are filled in from left to right.

1. Recurse down left and right trees
2. Check if the left side height and right side height are the same
    a. If they are the same, it is a perfect binary tree so return 2 ** height - 1
    b. If they aren't recurse down the subtree's left and right nodes
3. Add one to the return value to count the current subtree's root
'''

def does_nth_node_exist(root, n):
    return n <= number_of_nodes_in_complete_binary_tree(root)

def number_of_nodes_in_complete_binary_tree(root):
    if not root return 0

    left_height = left_height_of_binary_tree(root.left)
    right_height = right_height_of_binary_tree(root.right)

    if left_height == right_height:
        return 2 ** left_height - 1
    
    return number_of_nodes_in_complete_binary_tree(root.left) +
        number_of_nodes_in_complete_binary_tree(root.right) + 1

def left_height_of_binary_tree(root):
    if not root: return 1
    return left_height_of_binary_tree(root.left) + 1


def right_height_of_binary_tree(root):
    if not root: return 1
    return right_height_of_binary_tree(root.right) + 1