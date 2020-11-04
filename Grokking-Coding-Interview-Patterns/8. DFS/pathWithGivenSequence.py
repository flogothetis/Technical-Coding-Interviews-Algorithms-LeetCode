
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Time /Sp[ace Complexity : O(N)
def find_path_rec(root, sequence, subSeqIndex):
    if (root is None or subSeqIndex >= len(sequence)):
        return False

    found = False

    if ( root.val == sequence[subSeqIndex] and subSeqIndex == len(sequence)-1  and root.right is None
        and root.left is None):

        return True
    if (root.val == sequence[subSeqIndex] and subSeqIndex < len(sequence)):
        found = find_path_rec(root.left, sequence, subSeqIndex+1) or find_path_rec(root.right, sequence, subSeqIndex+1)

    return found


def find_path(root, sequence):
  subSeqIndex = 0
  return find_path_rec(root, sequence, subSeqIndex)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 1])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
