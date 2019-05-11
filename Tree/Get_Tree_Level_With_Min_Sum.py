from collections import defaultdict, deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def smallest_level(root):
    queue = deque([])
    queue.append((root, 0))

    # Create a map to accumulate the sum for each level.
    level_to_sum = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_to_sum[level] += node.data

        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))

    return min(level_to_sum, key=level_to_sum.get)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    print(smallest_level(root))
