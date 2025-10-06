def isValid(s):
    stack = []  # list for parentheses
    close_to_open = {")": "(", "]": "[", "}": "{"}  # a dictionary that maps closing parentheses to opening ones
    for i in s:  # for parentheses in string
        if i in close_to_open:  # if item is in dictionary ie is a closing one
            if stack and stack[-1] == close_to_open[i]:  # checks if stack is empty and if last item added to stack is its opening one
                stack.pop()  # if yes then removes the last item in the stack ie the opening one for the closing parentheses the index is on rn
            else:
                return False  # if stack is empty or the last one currently in the stack is not its opening counterpart  there should be no closing parentheses in the stack as a closing one would mean either it matches and pops or it fails
        else:
            stack.append(i)  # else if it's not a closing parentheses, then add item to stack
#    return True if not stack else False  # if stack is empty by the mean return true else return false
    if stack:
        return False
    else:
        return True  # same thing

print(isValid("[()]"))
print(isValid("[)"))
