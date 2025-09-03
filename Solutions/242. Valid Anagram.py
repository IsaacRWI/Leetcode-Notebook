# sorted solution
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

# optimised sorted solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# counter solution
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if Counter(s) == Counter(t): return True  # Counter creates a dictionary with the items in the list and the times its shown up
        return False

