'''
Target Sum (hard) #

You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.
'''


def find_target_subsets(num, s):
  return find_target_sum_rec(num, 0, s, len(num) -1, {})


# Time Comp : O( targetSum *
def find_target_sum_rec(array, sum, target_sum, index, memoi):
    if ((sum, index) in memoi):
        return memoi[(sum, index)]

    if (sum == target_sum and index <0 ):
        return 1
    elif (index < 0 ):
        return 0
    memoi[(sum, index)] = find_target_sum_rec(array, sum - array[index], target_sum, index -1, memoi) + \
           find_target_sum_rec(array, sum + array[index],  target_sum, index -1, memoi)

    return memoi[(sum, index)]
def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()

