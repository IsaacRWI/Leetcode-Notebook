# my solution
def twoSum(self, numbers, target):
    l = 0  # left pointer
    r = len(numbers) - 1  # right pointer
    while l < r:  # whilst they haven't overlapped
        # m = (l + r) // 2  # unused bit of code   middle only for binary search
        if numbers[l] + numbers[r] == target:  # if sum found then return 1-indexed index
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1  # move right pointer if sum is too big
        # elif l + r < taget:
        else:  # move left pointer if sum is too smaller
            l += 1

# optimised solution
    def twoSum(numbers, target):
        l, r = 0, len(numbers) - 1  # variables declared on 1 line
        while l < r:
            currSum = numbers[l] + numbers[r]  # sum declared at start of while loop for the loop
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return