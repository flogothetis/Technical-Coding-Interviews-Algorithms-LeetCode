

# Use hash map for unsorted array/list
def pairSumTarget (array, target):
	dictionary = {}
	for i in range(len(array)) :
		if array[i] in dictionary:
			return dictionary[array[i]], i
		dictionary[target - array[i]] = i
	return -1, -1

# Use two pointer for sorted array/list
def pairSumToTarget( sortedArray, target):
	startPointer = 0
	endPointer = len(sortedArray) - 1

	while  startPointer < endPointer:

		s = sortedArray[startPointer] + sortedArray[endPointer]
		if(s > target):
			endPointer -=1
		elif (s < target):
			startPointer +=1
		else:
			return startPointer, endPointer
	return -1, -1

def main():
  print(pairSumTarget([1, 2, 3, 4, 6], 6))
  print(pairSumTarget([2, 5, 9, 11], 11))


main()
