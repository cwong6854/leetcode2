class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Intuition
        # input -> array of integers, unsorted
        # 100 | 100 OR 4 | 100 OR 4 OR 200 | 100 OR 4 OR 200 OR 1 |
        # 3,4 | 1, 2, 3, 4
        # in input, are their duplicates?
        # for loop through nums -> store each number in set
        # for each number iterated, if number + 1 exist or number - 1 exist, add
        # hash map -> lets say there's 3, and 4 exists
        # then 3 -> 2, and 4 -> 2
        # iterate to 2, if 1 and 3 exists, hash[4] = hash[3] + hash[1] = 3 + 1 = 4
        # lets say 5, hash[5] = hash[4] + ... (6 doesn't exist) = 4 + 1
        # lets say 0, hash[0] = hash[1] + hash[-1]
        # 0, 1, 2, 3, 4, 5
        # 0,1,2,3 and 5,6,7,8  -> 4 comes in

        # AFTER LOOKING AT SOLUTION
        # if left neighbor of n does not exist in set, start of a sequence
        # while n + 1 exist, keep counting length


        # Time Complexity: 
        # O(N) -> visit each number at most once through set

        # Space Complexity: 
        # O(N) -> input of nums in set

        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
if __name__ == "__main__":
    solution = Solution().longestConsecutive
    assert(solution([100,4,200,3,1,2])==4)
    # Add your test cases here
    print("All test cases pass!")