'''



Problem Statement #

Given a set of numbers that might contain duplicates, find all of its distinct subsets.
'''

# Time Complexity : O(N* 2^N)
def find_subsets(nums):
  subsets = []
  subsets.append([])
  nums.sort()
  for i in range (len(nums)):
      n = len(subsets)
      counter = 0
      for subSet in range (n):
        if (i>0 and nums[i]== nums[i-1] and subSet < prev_counter ):
            continue
        s = list (subsets[subSet])
        s.append(nums[i])
        subsets.append(s)
        counter +=1
      prev_counter= counter


  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()