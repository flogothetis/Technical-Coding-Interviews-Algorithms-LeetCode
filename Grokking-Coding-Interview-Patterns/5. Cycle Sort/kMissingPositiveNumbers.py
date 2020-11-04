'''
Find the First K Missing Positive Numbers (hard) #

Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
'''

def find_first_k_missing_positive (num, k):
    i=0
    while (i < len(num)):
        j = num[i] - 1
        if (num[i]>0 and num[i] <= len(num) and num[i]!=num[j]):
            num[i], num[j]= num[j], num[i]
        else:
            i+=1

    k_missing_l = []
    non_sequential_numbers = set ()
    last_number_in_order = -1
    for i in range (len(num)):
        if (num[i] != i+1 ):
            k_missing_l.append(i+1)
            non_sequential_numbers.add(num[i])
        last_number_in_order = i+1


        if (len(k_missing_l) == k):
            return k_missing_l

    while (len(k_missing_l)!= k):
        last_number_in_order+=1
        if last_number_in_order not in non_sequential_numbers:
            k_missing_l.append(last_number_in_order)
    return k_missing_l


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()

