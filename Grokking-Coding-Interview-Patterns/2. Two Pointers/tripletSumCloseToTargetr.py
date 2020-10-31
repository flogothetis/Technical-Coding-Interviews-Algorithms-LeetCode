# Time Complexity :O(N)
def pairProblem (array, target,  low, high ):


	globalMin = float ('inf')
	minSum = 0;
	firstElementOfTriplet = array[low-1]

	while ( low < high ):

		curr_sum = array[low] + array[high]
		difference  = abs(target - curr_sum)
		if(globalMin > difference):
			globalMin = difference
			minSum = curr_sum + firstElementOfTriplet

		elif (globalMin  == difference):
			minSum = min(minSum, curr_sum + firstElementOfTriplet  )

		if (target > curr_sum):
			low+=1
		elif (target < curr_sum):
			high=-1
		else:
			break
	return  globalMin, minSum


# Time Complexity O(N^2 + NLogN)
def tripletSumProblem(array, target):
	#sort Array
	array = sorted(array) #

	globalMin = float ('inf')
	minSum = 0
	for i in range (len(array)):
		tripletMin, tripletSum = pairProblem(array, target - array[i], i+1, len(array)-1)

		if (globalMin > tripletMin):
			globalMin = tripletMin
			minSum = tripletSum

		elif (globalMin == tripletMin):
			minSum = min(minSum, tripletSum)
	return  minSum


def main():
  print(tripletSumProblem([-2, 0, 1, 2], 2))
  print(tripletSumProblem([-3, -1, 1, 2], 1))
  print(tripletSumProblem([1, 0, 1, 1], 100))


main()

