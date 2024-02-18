"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
      return x
  else:
      ra = foo(x - 1)
      rb = foo(x - 2)
      return ra + rb
    
print(foo(7))

def longest_run(mylist, key):
  count = 0
  max_count = 0
  for num in mylist: #iterates through the list
    if num == key: #If num = key, add 1 to count
      count += 1
      if count > max_count: #Checks if count is greater than max_count
        max_count = count #if so, max_count = count
    else: #Else reset count
      count = 0
  return max_count

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  n = len(mylist)

  #Base cases (when the list is empty or has only one element)
  if n == 0:
      return Result(0, 0, 0, False)
  if n == 1:
      if mylist[0] == key: # If the only element matches the key
          return Result(1, 1, 1, True)
      else:                #  Else:
          return Result(0, 0, 0, False)

  #Split the list into two halves
  mid = n // 2
  left = mylist[:mid]
  right = mylist[mid:]

  #Recursively find the longest run in both halves
  left_result = longest_run_recursive(left, key) #Output is Result object
  right_result = longest_run_recursive(right, key) #Output is Result object

  #Checks for runover at the boundry of split.
  #Creates new var cross_left_size, checks if left_result is entire range, if true, add left side of right_result.
  cross_left_size = left_result.left_size
  if left_result.is_entire_range:
      cross_left_size += right_result.left_size
  #Does the same as above for cross_right_size
  cross_right_size = right_result.right_size
  if right_result.is_entire_range:
      cross_right_size += left_result.right_size

  #Checks the cross longest size
  cross_longest_size = 0
  if mylist[mid - 1] == key and mylist[mid] == key: #checks at the boundry of split
      cross_longest_size = left_result.right_size + right_result.left_size

  #Updates new longest_size. Checks individual sizes plus the cross longest size. 
  longest_size = max(left_result.longest_size, right_result.longest_size, cross_longest_size)

  #Checks if the entire range is true
  is_entire_range = left_result.is_entire_range and right_result.is_entire_range

  return Result(cross_left_size, cross_right_size, longest_size, is_entire_range)
    

print(longest_run_recursive([6, 12, 12, 12, 12, 6, 6,], 12))

