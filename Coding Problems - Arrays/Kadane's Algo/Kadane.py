def kadane(array):
    if array is None:
        return  None

    if (len(array)==0):
        return None

    curr_sum=array[0]
    global_sum=curr_sum

    for i in range (1, len(array)):
        curr_sum= max(array[i], curr_sum + array[i])
        global_sum = max(global_sum, curr_sum)

    return  global_sum


#Driver code

print(kadane([-1,-2,-3,-4]))