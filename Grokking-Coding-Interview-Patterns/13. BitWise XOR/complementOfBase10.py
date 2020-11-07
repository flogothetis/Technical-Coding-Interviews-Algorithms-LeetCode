'''
Problem Statement #

Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.
'''

def calculate_bitwise_complement(n):
  num  = n
  # Count the numbers of bits of n
  counter = 0
  while ( num > 0) :
      num = num >> 1
      counter+=1
  # create a mask having the same number of bits
  # set to 1.
  mask = pow(2, counter) -1

  return mask ^ n

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()