'''
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find
the length of the longest substring having the same letters after replacement.



# Case 1:
window includes more than K letters that are not distinct --> reduce window

#Case 2:
window incorporates less or equal to K non distinct elements -> candidate

Idea : Hash Map to track the number of distinct elements
- Pass array once
'''

def longestSubKReplace (array, K):
	windowStartPointer = 0
	global_max_length = 0
	dictionary = {}
	for endWindowPointer in range (len(array)):
		if (array[endWindowPointer] in dictionary):
			dictionary[array[endWindowPointer]]+=1
		else:
			dictionary[array[endWindowPointer]] =1

		# Case 1
		while (endWindowPointer - windowStartPointer +1 - max(dictionary.values()) > K):
			dictionary[array[windowStartPointer]]-=1
			if (dictionary[array[windowStartPointer]] == 0):
				del dictionary[array[windowStartPointer]]
			windowStartPointer+=1
		#Case 2
		global_max_length = max (global_max_length, endWindowPointer - windowStartPointer +1)

	return global_max_length

def main():
  print(longestSubKReplace("aabccbb", 2))
  print(longestSubKReplace("abbcb", 1))
  print(longestSubKReplace("abccde", 1))


main()