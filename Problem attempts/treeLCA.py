def lowestCommonAncestor(root, p, q):
    nodes = pre_order(root)
    print(nodes)
                         


def pre_order(node):
    left_vals = []
    right_vals = []

    if node.left:
        left_vals += node.left.pre_order()
    
    center_root = [node]
    
    if node.right:
        right_vals+= node.right.pre_order()
    


    return [left_vals, center_root, right_vals]