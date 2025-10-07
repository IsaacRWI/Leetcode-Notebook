def productExceptSelf(self, nums):
    left_mult = 1  # value of numbers multiplied together  starting from the left
    right_mult = 1  # value of numbers multiplied together starting from the right
    n = len(nums)  # length of the list
    left_array = [0] * n  # array to store values as the multiplier multiplies the numbers in the list together
    right_array = [0] * n

    for i in range(n):
        j = -i - 1  # i will go down the list and j will go up the list from the last index
        left_array[i] = left_mult  # fill in the array with the current multiplied total of the values in the list
        right_array[j] = right_mult
        left_mult *= nums[i]  # multiply the current value into the multiplier for the next item   do this after setting the array because we want the product to not include the value its currently on in the array
        right_mult *= nums[j]

    return [l * r for l, r in zip(left_array, right_array)]  # multiplies the values in the two arrays together