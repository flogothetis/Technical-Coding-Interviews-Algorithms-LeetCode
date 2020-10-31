'''
Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find
the length of the longest contiguous subarray having all 1s.
'''

#Time Complexity: O(N)
#Space: O(1)
def longestSubArrayZeroReplace (array, numberofReplace):
	windowStart = 0
	dictionary ={}
	globalMaxLen = 0

	for windowEnd in range (len(array)):
		if (array[windowEnd] not in dictionary):
			dictionary[array[windowEnd]] = 0
		dictionary[array[windowEnd]]+=1

		while (dictionary.get(0,0)> numberofReplace):
			dictionary[array[windowStart]]-=1
			if (dictionary[array[windowStart]] == 0):
				del dictionary[array[windowStart]]
			windowStart +=1

		globalMaxLen = max(globalMaxLen, (windowEnd-windowStart+1))
	return globalMaxLen

def main():
  print(longestSubArrayZeroReplace([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(longestSubArrayZeroReplace([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()