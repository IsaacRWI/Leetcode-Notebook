def search( nums, target):
    l = 0
    r = len(nums) - 1  # -1 because index for list starts at 0
    while l <= r:  # mean they haven't crossed each other yet
        m = (l + r) // 2  # middle index
        if nums[m] > target:  # shifts l or r depending on target position
            r = m - 1
        elif nums[m] < target:
              l = m + 1
        else:
             return m  # return m when nums[m] == target
    return -1  # return -1 when l and r crossed and still didn't find target

print(search([-1,0,3,5,9,12], 9))
print(search([1,2,3],6))