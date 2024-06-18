class Solution(object):
    def productExceptSelf(self, nums):
        # Intuition
        # multiply prefix, then suffix -> create new array size of nums
        # with prefix -> skip 0 index
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr, res = 1, len(nums) * [1]
        # multiply with prefix, skip index 0
        for i in range(1, len(nums)):
            curr *= nums[i-1]
            res[i] *= curr
        curr = 1
        for i in range(len(res)-1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        return res

if __name__ == "__main__":
    solution = Solution().productExceptSelf
    assert(solution([1,2,3,4]))==[24,12,8,6]
    # Add your test cases here
    print("All test cases pass!")