def sort012(array):
    n=len(array)
    # Set low, and middle pointers
    l=m=0
    # Set high pointer
    h=n-1

    while(m<=h):
        if array[m]==0:
            array[m],array[l]=array[l],array[m]
            l+=1
            m+=1
        elif array[m]==1:
            m+=1
        else:
            array[h],array[m]= array[m],array[h]
            h-=1




# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(arr)
print(arr)