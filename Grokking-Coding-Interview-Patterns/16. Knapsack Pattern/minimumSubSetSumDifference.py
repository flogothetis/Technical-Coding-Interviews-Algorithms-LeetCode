'''
Problem Statement #

Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
'''



# Time Comp/Space Comp : O( sum ( array) , len(array))
def can_partition(array):
  counter = 0
  return can_partiotion_rec(array, 0 , 0, 0, {})


def can_partiotion_rec (array, sum1, sum2, numberIndex, memoization_dict):
    if ((sum1, numberIndex) in memoization_dict):
        return memoization_dict[(sum1, numberIndex)]

    if (numberIndex == len(array) ):
        return abs (sum2-sum1)


    memoization_dict[(sum1, numberIndex)] = min (can_partiotion_rec(array, sum1 + array[numberIndex], sum2, numberIndex+1, memoization_dict) ,
            can_partiotion_rec(array, sum1, sum2 + array[numberIndex], numberIndex+1, memoization_dict) )

    return  memoization_dict[(sum1, numberIndex)]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
