'''
Problem Statement #
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
'''

from collections import deque


def generateParenthesisRec(string, openPar, closePar, allCombination):
    if (openPar == 0 and closePar == 0):
        allCombination.append(string)
        return
    if (openPar> 0):
        generateParenthesisRec(string+'(', openPar -1, closePar, allCombination)
    if (closePar >0 and openPar < closePar):
        generateParenthesisRec(string+')', openPar, closePar - 1, allCombination)

def generate_valid_parentheses(num):
  result = []
  generateParenthesisRec("", num, num, result)
  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()