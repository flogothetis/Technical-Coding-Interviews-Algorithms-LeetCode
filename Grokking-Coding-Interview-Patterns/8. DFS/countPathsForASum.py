'''
Problem Statement #

Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values
of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow
 direction from parent to child (top to bottom).

'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Time Complexity :O(N^2)
# Space Complexity : O(N)
def count_paths_rec(root, S, current_path):
    if root is None:
        return 0
    current_path.append(root.val)
    pathSum, pathCount = 0, 0
    for i in range (len(current_path)-1 , -1 ,-1 ):
        pathSum += current_path[i]

        if (pathSum == S):
            pathCount+=1

    pathCount+= count_paths_rec(root.left, S, current_path)
    pathCount+= count_paths_rec(root.right, S, current_path)

    current_path.pop()
    return pathCount


def count_paths(root, S):
    curent_path = []
    return count_paths_rec (root, S, curent_path)



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
