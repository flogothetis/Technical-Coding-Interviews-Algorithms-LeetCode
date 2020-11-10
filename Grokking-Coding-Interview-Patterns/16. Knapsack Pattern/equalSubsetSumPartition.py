'''
Problem Statement #
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
'''


# Time Comp/Space Comp : O( sum ( array) , len(array))
def can_partition(array):
  counter = 0
  for num in array :
      counter+=num

  return can_partiotion_rec(array, counter/2 , len(array) -1, {})


def can_partiotion_rec (array, sum , numberIndex, memoization_dict):
    if ((sum, numberIndex) in memoization_dict):
        return memoization_dict[(sum, numberIndex)]

    if (sum == 0):
        return True
    if (numberIndex == 0 and array[numberIndex] == sum):
        return True
    elif (numberIndex ==0 and array[numberIndex] != sum):
        return False
    memoization_dict[(sum, numberIndex)] = can_partiotion_rec(array, sum -array[numberIndex], numberIndex-1, memoization_dict) or \
            can_partiotion_rec(array, sum, numberIndex-1, memoization_dict)

    return  memoization_dict[(sum, numberIndex)]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
