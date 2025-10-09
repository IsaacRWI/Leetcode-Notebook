# normal solution
def longestConsecutive(nums):
    numSet = set(nums)  # creates a set of the list so you dont have to run through duplicate values in the list
    longest = 0  # output value
    for i in numSet:  # for number in list
        if (i - 1) not in numSet:  # if theres not number thats 1 smaller than it is  ie it could be the beginning of a new sequence
            length = 1  # add 1 for itself
            while i + 1 in numSet:  # whilst there the next number is in the set
                length += 1  # add 1 to length
                i += 1  # add 1 to i
            longest = max(longest, length)  # check if length is longer than the longest we have and take max
    return longest


# leetcode accepted solution:
# code optimized for specific test case where there is like 100 values in the nums list and leetcode times out even with O(n) solutions
def longestConsecutive(nums):
    nums = set(nums)  # changing the type of the list directly instead of creating a new set variable for the list
    longest = 0
    for i in nums:
        if (i - 1) not in nums:
            next = i + 1  # creating a new variable for the next number in the sequence instead of just i + 1
            while next in nums:
                next += 1
            longest = max(longest, next - i)  # last number in sequence - first number to get length
    return longest
