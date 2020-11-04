'''
Problem Statement #

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
 Find the total sum of all the numbers represented by all paths.

'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Time Complexity : O(N)
# Space Complexity: O(N)
def find_sum_of_path_numbers_rec(root, sum):
    if root is None:
        return 0
    totalSum = 10* sum  + root.val
    if (root.left is None and root.right is None):
        return  totalSum

    return  find_sum_of_path_numbers_rec(root.left, totalSum) + find_sum_of_path_numbers_rec(root.right, totalSum)



def find_sum_of_path_numbers(root):

  return find_sum_of_path_numbers_rec(root, 0)






def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
