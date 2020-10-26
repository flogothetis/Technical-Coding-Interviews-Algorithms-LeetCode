# Time Complexity 4^N - Catalan - All possible po
def generateParenthesisRec (resultList, curr_str, countOpen, countClose ):

    if(countOpen == 0 and countClose == 0):
        resultList.append(curr_str)
    if countOpen>0:
        generateParenthesisRec(resultList, curr_str +'(', countOpen-1, countClose)

    if countOpen < countClose and countClose >0:
        generateParenthesisRec(resultList, curr_str + ')', countOpen, countClose-1)

#Driver Code
def generateParenthesis(n):
    resultList=[]
    generateParenthesisRec(resultList, "", n, n)
    return resultList

# Driver Code
n = 3
print(generateParenthesis(n))