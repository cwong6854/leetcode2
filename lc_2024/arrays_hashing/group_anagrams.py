"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# Intuition
# Categorize the groups into their respective letters that they contain
# EX: eat, tea -> aet

# Approach
# go through each element, sort the element's letters, and then store in hash map in a list
# return dictionary as a list based on its values

# Time Complexity
# O(n * k) -> only iterate through strs ONCE, where k is the longest string

# Space Complexity
# O(n * k)

# ADD CODE HERE
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            group = "".join(sorted(word))
            if group not in dic:
                dic[group] = [word]
            else:
                dic[group].append(word)
        return list(dic.values())

# Tests
if __name__ == "__main__":
    solution = Solution().groupAnagrams
    assert(solution(["eat","tea","tan","ate","nat","bat"])==[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
    # Add your test cases here
    print("All test cases pass!")