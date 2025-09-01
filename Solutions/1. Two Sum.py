class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}  # empty map for later use

        for i, n in enumerate(nums):  # enumerate allows for return of item and its index  i being index and n being the item
            delta = target - n  # delta ie the number we want, is the target (sum) - the item the for loop is on rn.  t=5 n=1 then x=5-1=4
            if delta in map:  # if the value we're looking for is already in the map,
                return [map[delta], i]  # then return it and the item in the for loop rn
            map[n] = i  # else add the item into the empty map with its index from the original list