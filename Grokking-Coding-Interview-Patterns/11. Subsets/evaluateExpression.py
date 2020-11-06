'''
Evaluate Expression (hard) #

Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be
evaluated by grouping the numbers and operators using parentheses.
'''

# Time Complexity : O(N ^ 2^N)
# Space Complexity : (2^N)
def diff_ways_to_evaluate_expression(input, memoizationMap):
    if input in memoizationMap:
        return memoizationMap[input]

    result = []
    if ( "+" not in input and "-" not in input and "*" not in input):
        result.append(int(input))
        return result
    for i in range(len(input)):
        ch = input[i]
        if not ch.isdigit():
            left_result = diff_ways_to_evaluate_expression(input[0:i], memoizationMap)
            right_result = diff_ways_to_evaluate_expression(input[i + 1:], memoizationMap)

            for left in left_result:
                for right in right_result:
                    if ch == '+':
                        result.append(left + right)
                    elif ch == '-':
                        result.append(left - right)
                    else:
                        result.append(left * right)
    memoizationMap[input] = result
    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3",{})))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5",{})))


main()
