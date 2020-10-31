'''
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is
to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree
until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.
'''

'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.
'''

def longestSubArrayKDistinct (array, K):

	startWindowPointer = 0

	dict_arr = {}
	longestSubArray = 0

	for endWindowPointer in range(len(array)):
		if (array[endWindowPointer] in dict_arr):
			 dict_arr[array[endWindowPointer]]+=1
		else:
			dict_arr[array[endWindowPointer]] = 1

		while (len(dict_arr)> K):
			if (dict_arr[array[startWindowPointer]] == 1):
				del dict_arr[array[startWindowPointer]]
			else:
				dict_arr[array[startWindowPointer]]-=1

			startWindowPointer+=1

		longestSubArray = max (longestSubArray, endWindowPointer - startWindowPointer +1)

	return longestSubArray


def main():
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct(['A', 'B', 'C', 'A', 'C'], 2)))
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct(['A', 'B', 'C', 'B', 'B', 'C'], 2)))

main()


