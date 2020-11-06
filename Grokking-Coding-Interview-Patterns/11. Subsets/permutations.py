'''
Problem Statement #

Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}

If a set has ‘n’ distinct elements it will have n! permutations.
'''

from collections import deque

# Time complexity : N * N!
def find_permutations(nums):
  result = []
  permutations = deque()
  permutations.append([])
  for num in nums:
      n = len(permutations)
      for _  in range (n):
          perm  = permutations.popleft()
          for j in range (len(perm) + 1):
              perm_copy  = perm.copy()
              perm_copy.insert(j, num)
              permutations.append(perm_copy)
              if(len(perm_copy) == len(nums)):
                  result.append(perm_copy)
  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
