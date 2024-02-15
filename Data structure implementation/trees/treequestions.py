
  
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
  

def treeIncludes(root, target):
    if root is None: return False
    if root.val == target: return True
    
    return treeIncludes(root.left, target) or treeIncludes(root.right, target)
    

def treeSum(root):
    if root is None: return 0
    
    curr_sum = root.val
    
    left_sum = treeSum(root.left) if root.left else 0
    right_sum = treeSum(root.right) if root.right else 0
    
    total = left_sum + right_sum + root.val
    
    return total
    

def treeMinVal(root):
    if root is None: return float('inf')
    min_left = treeMinVal(root.left)
    min_right = treeMinVal(root.right)
    
    return min(root.val, min_left, min_right)

def maxPathSum(root):
    
    if root is None: return float('-inf')
    if root.left == None and root.right == None: return root.val
    
    maxChildPath = max(maxPathSum(root.left), maxPathSum(root.right))
    
    return root.val + maxChildPath
    


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(maxPathSum(a))