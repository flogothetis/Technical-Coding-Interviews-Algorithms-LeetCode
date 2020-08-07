from collections import deque


def checkBalance(expr):
    stack = deque()
    availableChars = ['{', '(', '[']

    for char in expr:
        if char in availableChars:
            stack.append(char)
        else:
            if stack == deque([]):
                return False
            closingChar = stack.pop()
            if char == '}' and closingChar != '{':
                return False
            elif char == ')' and closingChar != '(':
                return False
            elif char == ']' and closingChar != '[':
                return False

    return True


# Driver Code
expr = "{()}}"
print(checkBalance(expr))
