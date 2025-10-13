def maxArea(nums):
    l = 0  # left pointer
    r = len(nums) - 1  # right pointer
    max_a = 0  # max area we have

    while l < r:  # whilst in bounds
        width = r - l  # width of the container
        height = min(nums[l], nums[r])  # height of the container
        area = width * height  # current area of container
        max_a = max(max_a, area)  # update max area if current area is larger than recorded largest

        if nums[l] > nums[r]:  # move the smaller pointer
            r -= 1
        else:
            l += 1
    return max_a

print(maxArea([1, 9, 8]))