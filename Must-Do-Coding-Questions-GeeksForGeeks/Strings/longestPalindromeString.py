


# Time Comp : O(N^2)
# Space Comp: O(N)
def longestPalindromeRec(array, i, j, memo):

    if((i,j) in memo):
        return memo[(i,j)]

    if (i==j or j-i == 1):
        return array[i] == array[j],  (j-i+1)

    isPalindrome1, length1 = longestPalindromeRec(array, i, j-1, memo)
    isPalindrome2, length2 = longestPalindromeRec(array, i+1, j, memo)
    if ( (isPalindrome2 or isPalindrome1) and array[i] == array[j]):
        memo[(i,j)] = (True, j-i + 1)

    else:
        memo[(i,j)] = (False, max(length2, length1))
    return memo[(i,j)]

string = "geeks"
print(longestPalindromeRec(string, 0, len(string)-1, {})[1])



