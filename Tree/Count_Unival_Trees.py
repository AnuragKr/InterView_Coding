import time
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_unival(root):
    return unival_helper(root, root.data)


def unival_helper(root, data):
    if root is None:
        return True

    if root.data == data:
        return unival_helper(root.left, data) and \
            unival_helper(root.right, data)

    return False


def count_unival_subtrees_naive(root):
    if root is None:
        return 0

    left = count_unival_subtrees_naive(root.left)
    right = count_unival_subtrees_naive(root.right)

    return 1 + left + right if is_unival(root) else left + right


def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Return the number of unival subtrees,and a Boolean for
# whether the root is itself a unival subtree


def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.data != root.left.data:
            return total_count, False
        if root.right is not None and root.data != root.right.data:
            return total_count, False
        return total_count + 1, True

    return total_count, False


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


if __name__ == "__main__":
    root = Node("a")
    root.left = Node("a")
    root.right = Node("a")
    root.left.left = Node("a")
    root.right.right = Node("a")
    root.right.right.right = Node("b")
    start = time.time()
    print(count_unival_subtrees(root))
    end = time.time()
    print(end - start)
    
