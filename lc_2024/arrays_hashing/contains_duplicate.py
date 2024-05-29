# Intuition
# Initially, the problem suggests checking for any duplicates in a list of numbers.
# A straightforward method is to use a set to track seen numbers, as sets automatically handle duplicates.

# Approach
# Iterate through each number in the list:
# 1. Check if the number is already in the set.
# 2. If not, add the number to the set.
# 3. If it is, a duplicate exists, and we return True.
# If we finish the loop without finding a duplicate, we return False.

# Complexity
# Time complexity:
# The time complexity is O(n) because we pass through the list once.
# Space complexity: is O(n) in the worst case when all numbers are unique and we store each one in the set.

# Code
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_dupl = set()  # Create a set to track seen numbers
        for n in nums:  # Iterate through each number
            if n not in is_dupl:  # If the number is not in the set, add it
                is_dupl.add(n)
            else:  # If the number is in the set, return True (duplicate found)
                return True
        return False  # If no duplicates are found, return False

if __name__ == "__main__":
    f = Solution().containsDuplicate
    assert(f([1,2,3,1]) == True)
    assert(f([1,2,3,4]) == False)
    assert(f([1,1,1,3,3,4,3,2,4,2]))
    assert(f([1]) == False)
    print("All test cases pass!")