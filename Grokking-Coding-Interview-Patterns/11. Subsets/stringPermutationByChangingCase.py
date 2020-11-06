'''

Problem Statement #

Given a string, find all of its permutations preserving the character sequence but changing case.
'''

from collections import  deque

#Time Complexity : N * 2^N
def find_letter_case_string_permutations(str):
  result = []
  permutations = deque ()
  permutations.append([])

  for ch in str :
      n = len(permutations)
      for i in range (n):
          perm  = permutations.popleft()
          perm_copy = list(perm)
          perm_copy2 = list(perm)
          if (ch.isdigit()):
              perm_copy.append(ch)
              permutations.append(perm_copy)

          else:
              perm_copy.append(ch)
              perm_copy2.append(ch.swapcase())
              permutations.append(perm_copy)
              permutations.append(perm_copy2)
  for perm in permutations:
      result.append(''.join(perm))


  return result


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
