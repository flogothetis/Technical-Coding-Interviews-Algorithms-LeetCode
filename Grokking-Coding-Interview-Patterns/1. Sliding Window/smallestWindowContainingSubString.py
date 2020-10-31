
def smallestWindowContainingSubString (array, pattern):

	# Put pattern in dictionary
	dictionary = {}
	for ch in pattern:
		if ch not in dictionary:
			dictionary[ch] = 0
		dictionary[ch]+=1

	windowStart = 0
	globalMinWindow  = len(array) + 1
	match_ch = 0
	for windowEnd in range (len(array)):
		if (array[windowEnd] in dictionary ):
			dictionary[array[windowEnd]]-=1
			if(dictionary[array[windowEnd]] == 0):
				match_ch+=1

		while(match_ch == len(pattern)):
			globalMinWindow = min (globalMinWindow, (windowEnd- windowStart +1))

			if(array[windowStart] in dictionary):
				if(dictionary[array[windowStart]] == 0):
					match_ch-=1
				dictionary[array[windowStart]]+=1
			windowStart+=1

	if (globalMinWindow <= len(array)):
		return globalMinWindow
	else:
		return 0

def main():
  print(smallestWindowContainingSubString("aabdec", "abc"))
  print(smallestWindowContainingSubString("abdbca", "abc"))
  print(smallestWindowContainingSubString("adcad", "abc"))

main()
