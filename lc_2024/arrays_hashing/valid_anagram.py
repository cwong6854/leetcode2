"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
# Intuition
# I would first iterate through s and put them in a hash to track how many times a letter is used, and keep their counts

# Approach
# Step-by-step description of your approach:
# 1. Create a dictionary for hashing letters and their counts
# 2. iterate through s and put each letter into the dictionary and track the counts of occurences
# 3. iterate through t and if letter is in dictionary and count greater than 0, subtract and continue till the END -> return True
# OTHERWISE -> return False
# Conclude what happens after all steps are executed.

# Complexity
# Time complexity:
# O(n) because we have 2 For Loops size N 

# Space complexity:
# Provide an analysis of the space complexity of your solution.

# ADD CODE HERE
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(t) < len(s): return False
        for l in s:
            dic[l] = dic.get(l, 0) + 1
        for l in t:
            if l in dic and dic[l] > 0:
                dic[l]-=1
                continue
            else:
                return False
        return True

        

# Tests
if __name__ == "__main__":
    solution = Solution().isAnagram # REPLACE
    # Add your test cases here
    assert(solution("anagram","nagaram")==True)
    assert(solution("rat","car")==False)
    assert(solution("tate","tater")==False)
    print("All test cases pass!")