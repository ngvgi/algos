class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

root = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')


root.left = b
root.right = c
b.left = d
b.right = e
c.right = f

"""
         5
    11      3
 4     2       1
 10
 """
num_tree_root = Node(5)
one = Node(1)
four = Node(4)
three = Node(3)
eleven = Node(11)
twelve = Node(12)
two = Node(2)
ten = Node(10)

num_tree_root.left = eleven
num_tree_root.right = three
three.right = one
eleven.left = four
eleven.right = two
four.left = ten



def dfs(root):
    if root == None:
        return []    
    
    nodes = [root.val]

    left_vals = dfs(root.left)
    right_vals = dfs(root.right)


    nodes += left_vals + right_vals
    
    return nodes

def bfs(root):
    if root == None:
        return []

    nodes = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        nodes.append(current.val)

        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return nodes

""" def bfs_belnizzo(root):

    if root == None:
        return []
    
    nodes = []
    nodes += [root.val]
    queue = [root]


    while len(queue) > 0:


        current = queue.pop(0)
        # nodes+= [current.val]

        level_items = []

        if current.left: 
            queue.append(current.left)
            level_items.append(current.left.val)
        if current.right: 
            queue.append(current.right)
            level_items.append(current.right.val)
        
        nodes += [level_items]


    return nodes



print(bfs_belnizzo(root)) """

def invertTree(root):
    if root == None:
        return []
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
    

def treeHasVal(root,target):
    if root == None:
        return False
    
    if root.val == target:
        return True

    return treeHasVal(root.left, target) or treeHasVal(root.right, target)

   

def treeSum(root):
    if root == None:
        return 0

    return root.val + treeSum(root.left) + treeSum(root.right)


def minTreeValBFS(root):
    if root == None:
        return 0
    
    queue = [root]
    min_val = root.val

    while len(queue) > 0:
        curr = queue.pop(0)
        curr_min = curr.val

        if curr_min < min_val:
            min_val = curr_min

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    return min_val



def minTreeValDFS(root):
    if root == None:
        return float('inf')

    return min(root.val, minTreeValDFS(root.left), minTreeValDFS(root.right))


def howManyBites(grams):
    if grams == 100:
        return 1
    
    return 1  + howManyBites(grams-100)
    

def maxPathSum(root):
    if root == None:
        return 0
    
    return max(root.val, root.val + maxPathSum(root.left), root.val + maxPathSum(root.right))

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth = 0):
            if root == None:
                return depth
            
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        
        return dfs(root)
        

""" def maxDepth(root,depth = 0):
    if root == None:
        return depth
    
    return max(maxDepth(root.left, depth+1), maxDepth(root.right, depth+1)) """


#####################################################################################################




""" 
G R A P H S
"""

# Adjacency list

graph ={
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def graphDFS(adj_list, start, nodes=[]):
    nodes.append(start)
   
    for neighbour in adj_list[start]:
        graphDFS(adj_list, neighbour)
    
    return nodes

def graphBFS(adj_list, start):
    queue = [start]

    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        queue+= adj_list[curr]
    
    return


def hasPath(graph, src, dest):
    if src == dest:
        return True
    
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest):
            return True
        
    return False

    
def hasPath(graph, src, dest, visited=set()):
    if src == dest:
        return True
    if src in visited:
        return False
    
    visited.add(src)

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest, visited):
            return True
        
    return False

def buildAdjList(edges):
    graph = {}

    for edge in edges:
        a = edge[0]
        b = edge[1]
        
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
      
    return graph


def connectedComponents(graph, visited = set(), count = 0):
    for node in graph:
        if exploreHelper(graph, node, visited):
            count += 1
    
    return count

def exploreHelper(graph, node, visited):
    if node in visited:
        return False
    
    visited.add(node)

    for neighbour in graph[node]:
        exploreHelper(graph, neighbour, visited )

    return True
    
countGraph = {
    0: [8, 1, 5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
}  


def largestComponent(graph, visited = set()):
    largest = 0

    for node in graph:
        curr_count = componentSize(graph, node, visited)
        if curr_count > largest:
            largest = curr_count

    return largest

def componentSize(graph, node, visited):
    if node in visited:
        return 0
    
    visited.add(node)
    count = 1

    for neighbour in graph[node]:
        count +=  componentSize(graph, neighbour, visited)
    
    return count


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

def numberOfIslands(grid, visited = set()):

    islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if exploreNeighbours(grid, row, col, visited):
                islands += 1


    return islands

def exploreNeighbours(grid, row, col, visited):
    if row < 0 or row >= len(grid):
        return False
    
    if col < 0 or col >= len(grid[0]):
        return False
    
    if grid[row][col] == 'W':
        return False
    
    if (row, col) in visited: 
        return False

    visited.add((row, col))
    

    exploreNeighbours(grid, row-1, col, visited) 
    exploreNeighbours(grid, row + 1, col, visited) 
    exploreNeighbours(grid, row, col - 1, visited) 
    exploreNeighbours(grid, row, col + 1, visited)
    
    return True
    

def minimumIslandCount(grid, visited = set()):
    smallest = float('inf')

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            curr_count = islandExplorer(grid, row, col, visited)
            if curr_count != 0 and curr_count < smallest:
                smallest = curr_count

    return smallest

def islandExplorer(grid, row, col, visited, count = 0):
    if row < 0 or row >= len(grid):
        return count
    
    if col < 0 or col >= len(grid[0]):
        return count
    
    if grid[row][col] == 'W':
        return count
    
    if (row, col) in visited:
        return count
    
    visited.add((row, col))

    count += 1

    count += islandExplorer(grid, row - 1, col, visited)
    count += islandExplorer(grid, row + 1, col, visited)
    count += islandExplorer(grid, row, col - 1 , visited)
    count += islandExplorer(grid, row, col + 1, visited)

    return count


    
######################################################################################################################

"""
Random problem attempts
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

""" def spiralOrder(matrix):
    if matrix == None:
        return 
    
    if len(matrix) == 1:
        return matrix[0]
    
    grid_size = len(matrix) * len(matrix[0])

    visited = set()
    elements = []
    row, col = 0, 0

    while len(visited) < grid_size:
        elements, row, col = traversalHelper(matrix, row, col, 'right', elements, visited)  
        elements, row, col = traversalHelper(matrix, row, col, 'down', elements, visited)
        elements, row, col = traversalHelper(matrix, row, col, 'left', elements, visited)
        elements, row, col = traversalHelper(matrix, row, col, 'up', elements, visited)

    return elements


def traversalHelper(matrix, row, col, direction, elements, visited ):

    if direction == 'left':
        while col >= 0:
            if (row, col) in visited:
                col -=1
                continue
            visited.add((row,col))
            elements.append(matrix[row][col]) 

            if col - 1 < 0:
                break

            col -=1
    
        return elements, row, col

    if direction == 'right':
        while col < len(matrix[0]):
            if (row, col) in visited:
                col +=1
                continue
            visited.add((row,col))
            elements.append(matrix[row][col]) 
            
            if col + 1 >= len(matrix[0]):
                break

            col +=1

        return elements, row, col

    if direction == 'up':
        while row >= 0:
            if (row, col) in visited:
                row-=1
                continue
            visited.add((row,col))
            elements.append(matrix[row][col]) 

            if row - 1 < 0:
                break

            row -=1
    
        return elements,row, col

    if direction == 'down':
        while row < len(matrix):
            if (row, col) in visited:
                row+=1
                continue
            visited.add((row,col))
            elements.append(matrix[row][col]) 

            if row + 1 >= len(matrix):
                break

            row +=1
    
        return elements, row , col
 """


def spiralOrder(matrix):
        result = []
        while matrix:
            result += matrix.pop(0) # Pop whole first row

            if matrix and matrix[0]: # 2 Pop last element of every row ('col')
                for line in matrix:
                    result.append(line.pop())

            if matrix: #3 Reverse pop elements from bottom row
                result += matrix.pop()[::-1]

            if matrix and matrix[0]: # 4
                for line in matrix[::-1]:
                    result.append(line.pop(0))
        return result




######################################################################################################

""" 
MICROSOFT CODILITY
"""


def traverse_grid(A, B):
    grid = [A, B]
    if not grid or not grid[0]:
        return 0
    
    rows, cols = 2, len(grid[0])
    
    # Initialize a 2xN memoization table to store optimal choices
    memo = [[0] * cols for _ in range(rows)]

    # Initialize the first cell in the memo table
    memo[0][0] = grid[0][0]

    # Fill the first row of the memo table
    for col in range(1, cols):
        memo[0][col] = min(memo[0][col - 1], grid[0][col])

    # Fill the memo table based on the optimal choices
    for row in range(1, rows):
        for col in range(cols):
            if col == 0:
                memo[row][col] = min(memo[row - 1][col], grid[row][col])
            else:
                memo[row][col] = min(max(memo[row - 1][col], memo[row][col - 1]), grid[row][col])

    # The bottom-right cell of the memo table contains the minimum value for the traversal
    return memo[1][cols - 1]

# Example usage:
A = [3,4,5]
B = [6,5,4]

""" result = traverse_grid(A, B)

print("Minimum value for traversal:", result) """


def solution(A, B):

    grid = [A,B]

    if not grid or not grid[0]:
        return 0
    
    rows, cols = 2, len(grid[0])
    
    # Initialize a 2xN memoization table to store optimal choices
    memo = [[0] * cols for _ in range(rows)]

    # Initialize the first cell in the memo table
    memo[0][0] = grid[0][0]

    # Fill the first row of the memo table
    for col in range(1, cols):
        memo[0][col] = max(memo[0][col - 1], grid[0][col])

    # Fill the memo table based on the optimal choices
    for row in range(1, rows):
        for col in range(cols):
            if col == 0:
                memo[row][col] = max(memo[row - 1][col], grid[row][col])
            else:
                memo[row][col] = max(min(memo[row - 1][col], memo[row][col - 1]), grid[row][col])

    # The bottom-right cell of the memo table contains the maximum value for the traversal
    return memo[1][cols - 1]




def min_substrings(input_str):
    seen_chars = set()
    substr_count = 0
    current_substr = ""

    for char in input_str:
        if char not in seen_chars:
            seen_chars.add(char)
            current_substr += char
        else:
            if current_substr:
                substr_count += 1
                seen_chars = {char}
                current_substr = char

    # Every unique character marks the end of a substring
    return substr_count + (1 if current_substr else 0)

# Example usage:
input_string = ""
result = min_substrings(input_string)





####################################################################################################


def maxProdArr(A, count = 0, prod_pos = 1, prod_neg = 1, digits = 3):
    if A is None:
        return
    
    
    largest_val = max(A)
    smallest_val = min(A)

    idx_smallest = A.index(largest_val)
    idx_largest = A.index(smallest_val)

    prod_pos *= largest_val
    prod_neg *= smallest_val

    count += 1
    maxProd = max(prod_pos, prod_neg)

    if len(A)>= idx_largest:
        A.pop(idx_smallest)

    if len(A)>= idx_largest: 
        A.pop(idx_largest)

    if count == digits:
        return maxProd
    
    else: 
        return maxProdArr(A, count, prod_pos, prod_neg)

   
        



A = [-5,-2,-1, 0,0,3,4,5]

print(maxProdArr(A))






