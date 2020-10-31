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
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct("araaci", 2)))
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct("araaci", 1)))
  print("Length of the longest substr1ing: " + str(longestSubArrayKDistinct("cbbebi", 3)))

main()


