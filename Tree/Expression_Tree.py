class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if root.data == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    elif root.data == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    elif root.data == TIMES:
        return evaluate(root.left) * evaluate(root.right)
    elif root.data == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.data

if __name__ == "__main__":
    root = Node("*")
    root.left = Node("+")
    root.right = Node("+")
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(5)
    root.right.left = Node(4)

    print(evaluate(root))   