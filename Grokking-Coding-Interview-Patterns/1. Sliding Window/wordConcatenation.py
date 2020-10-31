'''

Words Concatenation (hard) #
Given a string and a list of words, find all the starting indices of substrings in the given string that are
 a concatenation of all the given words exactly once without any overlapping of words. It is given that all
  words are of the same length.

'''

# Time Complexity : O (N*M)
# N : length of string
# M: total numbers of words
#Space : O (N + M) (hashMap and result list)
def wordConcatenation(string , words_l):

	dictionary = {}
	for word in words_l:
		if (word not in dictionary):
			dictionary[word] = 0
		dictionary[word]+=1


	windowStart = 0
	word_size = len(words_l[0])
	matches = 0
	startIndicesList = []
	for windowEnd in range(word_size, len(string) +1 , word_size):
		if(string[windowEnd-word_size:windowEnd] in dictionary):
			dictionary[string[windowEnd-word_size:windowEnd]]-=1
			if dictionary[string[windowEnd-word_size:windowEnd]] == 0:
				matches +=1
			elif(dictionary[string[windowEnd-word_size:windowEnd]] < 0):
				dictionary[string[windowStart:windowStart + word_size]] += 1
				windowStart += word_size
				continue
		else:
			dictionary[string[windowStart:windowStart+word_size]]+=1
			windowStart+=word_size
			continue


		if (matches == len(words_l)):
			startIndicesList.append(windowStart)
			dictionary[string[windowStart:windowStart+word_size]]+=1
			matches -= 1
			windowStart += word_size
	return startIndicesList

def main():
  print(wordConcatenation("catfoxcat", ["cat", "fox"]))
  print(wordConcatenation("catcatfoxfox", ["cat", "fox"]))



main()