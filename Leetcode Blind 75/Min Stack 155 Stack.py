class MinStack:

    def __init__(self):
        self.stk = []  # main stack
        self.mstk = []  # stack keeping track of min value in stack

    def push(self, val: int) -> None:
        self.stk.append(val)  # add value to main stack

        if not self.mstk:  # if min stack is empty
            self.mstk.append(val)
        elif self.mstk[-1] < val:  # if the last element in the min stack (-1 index means last value) is larger than new value
            self.mstk.append(self.mstk[-1])  # add the smaller one alr in the stack again  this is so even if they pop values we can just pop the index from both stacks and dont bother
        else:
            self.mstk.append(val)  # add the new value if its smaller than what we have in our min stack

    def pop(self) -> None:
        self.stk.pop()  # pop removes the last element in the list
        self.mstk.pop()

    def top(self) -> int:
        return self.stk[-1]  # return last element in main stack

    def getMin(self) -> int:
        return self.mstk[-1]  # return last element in min stack

