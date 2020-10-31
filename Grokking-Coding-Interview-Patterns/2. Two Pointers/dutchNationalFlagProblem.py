
#  Time complexity : O(N)
# Space : O(1)
def sort012 (array):

	pointer0  = 0
	pointer1=  pointer0
	pointer2  = len(array) -1

	while (pointer1 <= pointer2):
		if(array[pointer1] == 0 ):
			array[pointer0], array[pointer1]= array[pointer1], array[pointer0]
			pointer0 +=1
			pointer1+=1

		elif (array[pointer1] == 1):
			pointer1+=1

		else:
			array[pointer1], array[pointer2]= array[pointer2], array[pointer1]
			pointer2-=1



def main():
  arr = [1, 0, 2, 1, 0]
  sort012(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  sort012(arr)
  print(arr)


main()


