'''
Problem Statement
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from
the root node to the nearest leaf node.
'''



class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def find_minimum_depth(root):
  if (root is None) :
      return 0
  if (root.right is None):
    return find_minimum_depth(root.left) + 1
  if( root.left is None):
    return find_minimum_depth(root.right) +1

  return min (find_minimum_depth(root.left) , find_minimum_depth(root.right)) + 1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
