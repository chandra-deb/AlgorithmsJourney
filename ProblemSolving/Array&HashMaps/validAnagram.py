# https://leetcode.com/problems/valid-anagram/description/


class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        for key, value in s_map.items():
            if t_map.get(key, 0) != value:
                return False
        return True

        
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_set = {}
        t_set = {}
        for l in s:
            s_set[l] = s_set.get(l,0) + 1
        for l in t:
            t_set[l] = t_set.get(l,0) + 1
        
        for key, value in s_set.items():
            if t_set.get(key, 0) != value:
                return False
        return True
        
        
# Solution 2 took less time then Solution 1 
# even though I altogether used 3 loops here. Why!?
'''Maybe accessing the values using index is taking the time??'''


# After Exploring Better Solutions
'''I got one where instead of creating two hash_maps for s and t
he just did it for one string s and then he loop over t
and while looping he check whether the single character is in the
hash_map(we got from s). If it is, then he subtract 1 from the hash_map[character]
value. After this loop finishes then he loop over the value of the has_map,
and if he find any value != 0 then he return False.
if All of them are 0 then he return True. 
Actually this solution is also trivial
'''

'''I got another one which take advantage of the count method of string.
It runs really fast. Anyway I don't know how the count method is implemented.
The Solution is:
'''



class Solution4(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        #It took 2911ms without converting to set...
        #After converting to set it became 2ms!!! Whooah! 
        for l in set(s): 
            if s.count(l) != t.count(l):
                return False
        return True


        