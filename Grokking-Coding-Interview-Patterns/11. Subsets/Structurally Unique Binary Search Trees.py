

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Time Complexity: O(N^2)
# Space Complexity: O(N)
def find_unique_trees(n, map ):
    if (n in map):
        return map[n]
    result = []
    if (n<=1):
        return 1
    elif (n==2):
        return  2

    for i in range (0, n):
        res = find_unique_trees(i,map) * find_unique_trees(n-1-i,map)
        result.append(res)
    map[n] = sum (result)
    return sum(result)




def main():
  print("Total trees: " + str(find_unique_trees(4, {})))
  print("Total trees: " + str(find_unique_trees(3, {})))


main()
