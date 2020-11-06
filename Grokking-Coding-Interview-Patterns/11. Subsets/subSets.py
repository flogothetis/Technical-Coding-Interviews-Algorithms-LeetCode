'''
Given a set with distinct elements, find all of its distinct subsets.
'''

# Time Complexity : O(N* 2^N)
def find_subsets(nums):
  subsets = []
  subsets.append([])
  for i in range (len(nums)):
      n = len(subsets)
      for subSet in range (n):
        s = list (subsets[subSet])
        s.append(nums[i])
        subsets.append(s)


  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
