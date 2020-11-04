'''
Tree Diameter (medium) #

Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the
 longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

'''
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.treeDiameter = 0

  def find_diameter(self, root):
      self.find_diameter_rec(root)
      return self.treeDiameter

  def find_diameter_rec (self, root):
    if (root is None):
        return 0

    left_height = self.find_diameter_rec(root.left)
    right_height = self.find_diameter_rec(root.right)
    self.treeDiameter = max (self.treeDiameter, left_height+right_height+1)
    return max(left_height, right_height) + 1



def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()







