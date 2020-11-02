
'''
Target : Determine if their is a cycle

# Restrictions :
1. Cycle must have more than one element
2. Only one direction (either forward or backward)

Basic Idea ....
1. Check each element for a cycle ( slow and fast pointer)
2. Check if the cycle obey to the restrictions
'''

VISITED = 2
VISITING = 1
NOT_VISITED = 0

# O(N)
def dfsUtil(array, i, colors):
    colors[i] = VISITING
    next_step = (array[i] + i  + len(array)) % len(array)


    if (colors[next_step] == VISITED or array[i] * array[next_step] < 0):
        return  False
    elif (colors[next_step] == VISITING):
        result = next_step != i
    else:
        result = dfsUtil(array, next_step, colors)
    colors[i] =VISITED
    return result


def simpleDFS (array):

    colors = [0] * len(array)
    for i in range (len(array)):
        if (colors[i] == NOT_VISITED):
            if( dfsUtil (array, i , colors)):
                return True
    return False

def findNextIndex(array, startIndex, isForward):

    newIndex = (startIndex + array[startIndex]) % len(array)

    # Restriction 1
    if  newIndex == startIndex:
        return  -1
    # Restriction 2
    isNewStepForward = array[startIndex] >=0
    if isNewStepForward != isForward :
        return -1
    return newIndex




def checkforCyrcle(array, startIndex, isForward, visited):
    slow, fast = startIndex, startIndex
    visited[slow] = True
    while True :
        slow = findNextIndex(array, slow, isForward)
        fast = findNextIndex(array, fast, isForward)
        if fast !=-1:
            fast = findNextIndex(array, fast, isForward)
            visited[fast] = True
        if (visited[slow] != -1):
            visited[fast] = True
        if (slow == -1 or fast == -1 or slow == fast):
            break
    if (slow !=-1 and slow == fast):
        return True
    return False


# Time Complexity O(N)
def isCircularArray (array):

    visited = [False] * len(array)

    if ( len(array) == 1 ):
        return False

    for i in range (len(array)):
        if (visited[i]):
            continue
        if (checkforCyrcle(array, i, array[i]>=0, visited)):
            return True
    return False


def main():
  print(simpleDFS([1, 2, -1, 2, 2]))
  print(simpleDFS([2, 2, -1, 2]))
  print(simpleDFS([2, 1, -1, -2]))


main()