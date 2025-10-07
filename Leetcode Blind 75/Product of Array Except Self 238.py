def productExceptSelf(self, nums):
    left_mult = 1
    right_mult = 1
    n = len(nums)
    left_array = [0] * n
    right_array = [0] * n

    for i in range(n):
        j = -i - 1
        left_array[i] = left_mult
        right_array[j] = right_mult
        left_mult *= nums[i]
        right_mult *= nums[j]

    return [l * r for l, r in zip(left_array, right_array)]