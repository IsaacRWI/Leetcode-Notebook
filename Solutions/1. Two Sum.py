class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i, n in enumerate(nums):  # enumerate allows for return of item and its index  i being index and n being the item
            delta = target - n
            if delta in map:
                return [map[delta], i]
            map[n] = i