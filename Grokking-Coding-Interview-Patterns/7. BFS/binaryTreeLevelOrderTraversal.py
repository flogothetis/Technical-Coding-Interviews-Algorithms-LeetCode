'''
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of
all nodes of each level from left to right in separate sub-arrays.
'''

from collections import  deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

# Time Complexity : O(N)
# Space : O(N)
def traverse(root):
  result = []

  if (root is None):
      return result

  q = deque()
  q.append(root)


  while q:
      # queue size
      levels = len(q)
      current_level = []
      for _ in range (levels):
          current_node = q.popleft()

          if current_node.left :
              q.append(current_node.left)
          if current_node.right :
              q.append(current_node.right)
          current_level.append(current_node.val)
      result.append(current_level)
  return result




def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
