class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = ""  # longest common prefix
        for i in range(len(strs[0])):  # for every letter in the first word in the list
            for s in strs:  # for every word in the string
                if i == len(s) or s[i] != strs[0][i]:  # if the index is equal to length of word ie out of bounds or the ith letter for s != to the ith letter for the first word in list
                    return longest  # return longest as output to function
            longest += strs[0][i]  # if the ith letters equal, add the ith letter to longest
        return longest  # if they are all equal then return longest
