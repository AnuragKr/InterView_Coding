from BT_Insert_Find_Op import BST as BST
def get_bounds(root,x,floor=None,ceil=None):
    if not root:
        return floor,ceil
    
    if x == root.data:
        return x,x
    
    elif x < root.data:
        floor,ceil = get_bounds(root.left,x,floor,root.data)
    elif x > root.data:
        floor,ceil = get_bounds(root.right,x,root.data,ceil)
    
    return floor,ceil

if __name__ == "__main__":
    bst = BST()
    for _ in range(5):
        x = input("Enter Element:")
        bst.insert(x)
    print(get_bounds(bst.root,7))

        