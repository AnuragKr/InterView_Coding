class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None

    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    # We assume that elements of the input lists are tree nodes.
    root = Node(preorder[0])
    root_i = inorder.index(root.data)
    root.left = reconstruct(preorder[1:1+root_i], inorder[0:root_i])
    root.right = reconstruct(preorder[1+root_i:], inorder[1+root_i:])
    return root


def inorder_traversal(root):
    if root:
        print(root.data)
        inorder_traversal(root.left)
        inorder_traversal(root.right)


if __name__ == "__main__":
    preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
    new_root = reconstruct(preorder, inorder)
    inorder_traversal(new_root)
