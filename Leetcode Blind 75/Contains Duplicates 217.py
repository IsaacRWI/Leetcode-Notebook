def containsDuplicate(nums):
    st = set(nums)
    if len(st) != len(nums):
        return True
    else:
        return False

print(containsDuplicate([1,1,2,3,4]))
print(containsDuplicate([1,2,3,4]))