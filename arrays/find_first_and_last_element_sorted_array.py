class TestSolution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # [5,7,7,8,8,8,10], target = 8
        l, r = 0, len(nums) - 1
        if len(nums) == 0:
            return [-1, -1]
        while l < r:
            if nums[l] != target:
                l += 1
            if nums[r] != target:
                r -= 1
            if nums[l] == target and nums[r] == target:
                return [l, r]
        if nums[l] == target and nums[r] == target:
            return [l, r]
        else:
            return [-1, -1]

if __name__ == '__main__':
    lst = [1]
    t = 1
    TestSolution.searchRange(lst, t)