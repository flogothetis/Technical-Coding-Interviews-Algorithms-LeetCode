'''
Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the
duplicates in-place return the length of the subarray that has no duplicate in it.
'''
# Time Complexity : O(N)
# Space: O(1)
def removeDuplicates (array):
	nonDuplicate = 1
	i=1

	while(i< len(array)):
		if array[nonDuplicate-1] != array[i]:
			array[nonDuplicate-1] = array[i]
			nonDuplicate+=1
		i+=1

	return nonDuplicate



def main():
  print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
  print(removeDuplicates([2, 2, 2, 11]))


main()
