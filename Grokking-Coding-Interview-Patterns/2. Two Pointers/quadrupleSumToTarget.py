
# Time Complexity: O(N^3)
def quadrupleSumToTarget(array, target):

	array = sorted (array)

	result = []
	for i in range(len(array)-3):
		for j in range(i+1, len(array)-2):
			#avoid duplicates
			if( j>=1 and array[j] == array [j-1]):
				continue

			low, high = j+1, len(array)-1
			while (low < high):
				if (array[low] + array[high] + array[i] +array[j] < target):
					low+=1
				elif(array[low] + array[high] + array[i] +array[j] > target ):
					high-=1
				else:
					result.append([array[i], array[j], array[low], array[high]])
					low += 1
					high -= 1
					# avoid duplicates
					while (low < high and array[low]  == array [low-1]):
						low+=1
					while (low < high and array[high] ==  array[high+1]):
						high-=1



	return result





def main():
  print(quadrupleSumToTarget([4, 1, 2, -1, 1, -3], 1))
  print(quadrupleSumToTarget([2, 0, -1, 1, -2, 2], 2))


main()

