def findAllMissingNumbers(array):
    i = 0
    while (i < len(array)):
        j = array[i] - 1
        if i>=len(array) or j>=len(array):
            i+=1
            continue
        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1

    missing_l = []
    for i in range(len(array)):
        if (i + 1 != array[i]):
            missing_l.append(i + 1)
    return missing_l


print(findAllMissingNumbers([2, 1, 4, 5, 3, 5]))
