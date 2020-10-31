
def tripletWithSmallerSum (array , target):

	# Sort array
	array  = sorted(array)
	counter = 0

	for i in range ( len(array)):

		low, high  = i+1, len(array)-1
		while (low < high):

			if ( array[i] + array[low] + array[high] < target):
				counter += (high - low)
				low+=1
			else:
				high-=1

	return counter


def main():
  print(tripletWithSmallerSum([-1, 0, 2, 3], 3))
  print(tripletWithSmallerSum([-1, 4, 2, 1, 3], 5))


main()


