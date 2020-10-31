'''

Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
'''
# Triplet X + Y + Z  = 0
# Unique

# Already know pair sum to target X + Y = - Z


def pairSumToTarget (sortedArray, target, startPointer, result):

	dictionary ={}
	i= startPointer
	while(i<len(sortedArray)) :
		dictionary [target - sortedArray[i]] = sortedArray[i]
		if (sortedArray[i] in dictionary):
			result.append([dictionary[sortedArray[i]], sortedArray[i], -target])
			while (i<len(sortedArray) and sortedArray[i] == sortedArray[i-1]):
				i+=1
		i+=1
def findTriplets (array):
	sortedArray = sorted(array)
	result = []
	for i in range ( len(sortedArray)):
		if ( i>0 and sortedArray[i]== sortedArray[i-1]):
			continue
		pairSumToTarget(sortedArray, -sortedArray[i], i+1, result)
	return  result


def main():
  print(findTriplets([-3, 0, 1, 2, -1, 1, -2]))
  print(findTriplets([-5, 2, -1, -2, 3]))


main()