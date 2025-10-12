def threeSum(nums):
    nums.sort()  # sorts the numbers in the list so we can get a dataset viable for two pointers
    ans = []  # list of list of numbers that add up to 0
    for i in range(len(nums)):  # for indexes in list nums
        if nums[i] > 0:  # if its not the first element in the list
            break  # breaks out of this loop to the one below
        elif i > 0 and nums[i] == nums[i - 1]:  # its not the first element in the list and the number we're on is the same one we're on for the last one
            continue  # starts the loop again on the step number

        low = i + 1  # low pointer  ie the next number in the list after the i we're on rn
        high = len(nums) - 1  # high pointer
        while low < high:  # whilst the pointers have not passed each other
            summ = nums[i] + nums[low] + nums[high]  # sum of the current index along with the high and low pointers
            if summ == 0:  # if sum is 0 and we've found our list
                ans.append([nums[i], nums[low], nums[high]])  # add ans list to list
                low += 1  # move the pointers closer to the center
                high -= 1
                while low < high and nums[low] == nums[low - 1]:  # whilst not overlapped and the low number we're on rn is the same as the last one
                    low += 1  # move the pointer towards the center by 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
            elif summ < 0:  # else if its a new number and sum is too small
                low += 1  # move low pointer towards the center ie increase the lower pointer
            else:  # else if the new number sum is too large
                high -= 1  # move the high point towards the center ie decreasing the sum
    return ans