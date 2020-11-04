'''
Problem Statement #
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''



class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Time Complexity : In the worst case is list will be skewed (list). Hence, the algorithm
# will be traverse N nodes. Futhermore, the copy () operation costs O(N) since the hard copy of
# every node is needed.

#Space Complexity :
# curr_path : max path = number of leaves (N+1)/ 2  = O(N)
# all_paths stores O(N) paths of logN nodes-> totally O(NLogN)
def find_paths_rec(root, sum, curr_path, allPaths):
    if (root is None):
        return
    curr_path.append(root.val)

    if (root.val == sum and root.left is None and root.right is None):
        allPaths.append(curr_path.copy())

    else:
        find_paths_rec(root.left, sum-root.val, curr_path, allPaths )
        find_paths_rec(root.right, sum-root.val, curr_path, allPaths )

    del  curr_path[-1]



def find_paths(root, sum):
  allPaths = []
  find_paths_rec(root, sum , [], allPaths)
  return allPaths


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))\




main()
