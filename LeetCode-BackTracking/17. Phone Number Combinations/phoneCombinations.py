phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
# Time complexity 3^N x $ 4xN
def phoneCombRec(string :str, next_digit, results):
    if len(next_digit) == 0:
        results.append(string)
        return

    for i in (phone[next_digit[0]]):
        phoneCombRec(string + i, next_digit[1:], results)

#Driver Code
results= []
input_digits= "23945"
phoneCombRec("",input_digits, results)
print(results)