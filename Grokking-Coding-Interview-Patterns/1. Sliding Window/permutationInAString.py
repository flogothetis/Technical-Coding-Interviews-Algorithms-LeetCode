'''
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

'''

# Time Complexity : O(N+K)
# N: number of characters in string
# K: number of characters in pattern
# Space : O(K)
def permutationStringMatchPattern (array, pattern):

	if (len(array)<len(pattern)):
		return False

	# Put pattern's characters in HashMap
	dictionary = {}
	for i in pattern:
		if (i not in dictionary):
			dictionary[i] = 0
		dictionary[i]+=1

	windowStart = 0
	numberofMatches = 0;
	for windowEnd in range (len(array)):

		if (array[windowEnd] in dictionary):
			dictionary[array[windowEnd]]-=1
			if (dictionary[array[windowEnd]] == 0):
				numberofMatches +=1
		if(numberofMatches == len(dictionary)):
			return True

		if((windowEnd-windowStart+1) > len(pattern) -1 ):
			if (array[windowStart] in dictionary):
				if(dictionary[array[windowStart]]==0):
					numberofMatches-=1
				dictionary[array[windowStart]]+=1
			windowStart+=1
	return False

def main():
  print('Permutation exist: ' + str(permutationStringMatchPattern("oidbcaf", "abc")))
  print('Permutation exist: ' + str(permutationStringMatchPattern("odicf", "dc")))
  print('Permutation exist: ' + str(permutationStringMatchPattern("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(permutationStringMatchPattern("aaacb", "abc")))


main()
