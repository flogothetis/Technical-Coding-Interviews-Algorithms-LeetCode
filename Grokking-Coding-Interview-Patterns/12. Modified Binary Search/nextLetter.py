'''
Problem Statement #

Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also
means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
Write a function to return the next letter of the given ‘key’.
'''


# Time Complexity :O(N)
#Space Complexity: O(1)
def search_next_letter(letters, key):
    start, end = 0, len(letters) - 1
    if (key < letters[0] or key > letters[end]):
        return letters[0]
    while (start <= end):
        mid = start + (end - start) // 2
        if (letters[mid] < key):
            start = mid + 1
        else:
            end = mid - 1

    return letters[start]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()