def search( nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
              l = m + 1
        else:
             return m
    return -1

print(search([-1,0,3,5,9,12], 9))
print(search([1,2,3],6))