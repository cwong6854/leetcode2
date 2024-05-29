"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

# Intuition
# a + b = target -> a = target - b, store a and iterate through nums until we find a with the index

# Approach
# Step-by-step description of your approach:
# 1. Create a hash map that stores a: index
# 2. iterate through nums and store a: index
# 3. if a in hash map, then return current index with a such as [hash[a], i], else continue
# Conclude what happens after all steps are executed.


# Complexity
# Time complexity:
# Provide an analysis of the time complexity of your solution.

# Space complexity:
# Provide an analysis of the space complexity of your solution.

# ADD CODE HERE
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            b = nums[i]
            a = target - b
            if a in dic:
                return [dic[a], i]
            else:
                dic[nums[i]] = i
            

# Tests
if __name__ == "__main__":
    solution = Solution().twoSum # REPLACE
    # Add your test cases here
    assert(solution([2,7,11,15],9)==[1,0] or solution([2,7,11,15],9)==[0,1])
    assert(solution([3,4,5],8)==[0,2] or solution([3,4,5],8)==[2,0])    
    print("All test cases pass!")