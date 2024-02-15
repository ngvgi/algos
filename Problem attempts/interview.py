# Given a list of "greater than" pairs, return a bool to indicate whether the list of pair comparisons given are valid.

# a > b, b > c => true
# a > b, c > a, b > c, d < a => false

""" input: confirmed pairs
output: bool if there is no conflict with the confirmed pairs given as input

if el.A > both el.B and el. C, there should be no instance of el.C being greater than el.A

a: [b]
c: [a, b]
b: [c]
 """



pairs = [ ('a' , 'b'), ('b','c')]

# if a > b, a > c, what is hash?
# a: [b, c]


def validatePairs(pairs):
  if not pairs:
    return True
  
  # create_dict of element:[vals it is greater than]
  hash = {}
  
  for i in range(pairs):
    hash[pairs[i][0]] = hash.get(pairs[i][0], []) + pairs[i][1] # adding to hash
    
    if hash[pairs[i][1]] in hash: 
      if pairs[i][0] in hash[pairs[i][1]]:
        return False
      
      hash[pairs[i][0]].append(hash[pairs[i][1]]) # appending all other children curr val may be greater than
  
  return True
      
      
      
      
    
  
  




