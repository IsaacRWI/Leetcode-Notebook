def evalRPN(tokens):
    stack = []  # empty list as stack
    for i in tokens:
        if i == "+":  # if the item is an operator
            stack.append(stack.pop() + stack.pop())  # pop the last 2 items in the stack and add the sum of them back into the stack
        elif i == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b - a))
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        elif i == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))  # doing int on the result for the division rounds it down to the nearest whole number
        else:  # if the items is not an operator
            stack.append(int(i))  # add it to the stack
    return stack[0]  # return the only item in the stack

print(evalRPN(["2","1","+","3","*"]))