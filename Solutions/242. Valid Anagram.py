class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)  # turns the string s into a sorted list
        t = sorted(t)  # same for t
        if s == t:  # if the two sorted lists are the same then return true
            return True
        else:
            return False


