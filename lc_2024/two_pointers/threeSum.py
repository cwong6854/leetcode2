class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Intuition
        # elements -> negatives, zero, positives
        # dont want duplicate three sums -> sort list -> O(N)
        # check left neighbor, if duplicate then continue
        # Method
        # three_sum == 0, append
        # for loop -> while we're on element, use left and right pointers
        # if left index and left neighbor are same, keep incrementing left

        nums = sorted(nums) # O(n)
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: # checking left neighbor duplicate
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # check left neighbor for l and l cannot pass r for index range
                        l += 1
        return res
if __name__ == "__main__":
    solution = Solution().threeSum
    assert(solution([-1,0,1,2,-1,-4])==[[-1,-1,2],[-1,0,1]])
    # Add your test cases here
    print("All test cases pass!")