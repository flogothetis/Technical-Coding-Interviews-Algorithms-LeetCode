'''


Problem Statement #
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.\
 ind the two numbers that appear only once.
'''


def find_single_numbers(nums):
  xXORy = 0
  for i in nums:
      xXORy= xXORy ^ i

  rightMostSetBit  = 1

  # Shift until finding the bit that is 1. In that position the x and y
  # numbers differ.
  while  (xXORy & rightMostSetBit) == 0:
      rightMostSetBit= rightMostSetBit << 1

  num1, num2 = 0, 0

  for i in nums :
      if ( (i & rightMostSetBit)!= 0):
          num1= num1 ^ i
      else:
          num2= num2 ^ i
  return [num1, num2]


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()
