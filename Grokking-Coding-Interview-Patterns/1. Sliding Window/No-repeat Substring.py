'''
Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.
'''
# Time Complexity : O(N)
# Space O(1)  constant number of characters
def longestSubArrayKDistinct (array):

	startWindowPointer = 0

	dict_arr = {}
	longestSubArray = 0

	for endWindowPointer in range(len(array)):

		while (array[endWindowPointer] in dict_arr):
			del dict_arr[array[startWindowPointer]]
			startWindowPointer+=1

		dict_arr[array[endWindowPointer]] = 1
		longestSubArray = max (longestSubArray, endWindowPointer - startWindowPointer +1)

	return longestSubArray


def main():
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct("aabccbb")))
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct("abbbb")))
  print("Length of the longest substring: " + str(longestSubArrayKDistinct("abccde")))

main()


