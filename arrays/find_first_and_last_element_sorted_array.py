class TestSolution(object):
    def searchRange(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1
        # Runtime: O(N)

        # [5,7,7,8,8,8,10], target = 8
        # l, r = 0, len(nums) - 1
        # if len(nums) == 0:
        #     return [-1, -1]
        # while l < r:
        #     if nums[l] != target:
        #         l += 1
        #     if nums[r] != target:
        #         r -= 1
        #     if nums[l] == target and nums[r] == target:
        #         return [l, r]
        # if nums[l] == target and nums[r] == target:
        #     return [l, r]
        # else:
        #     return [-1, -1]

        # Solution 2
        # Runtime: O(log n)
        
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        first, last = 0, 0
        if len(nums) == 0:
            return [-1, -1]
        if nums[mid] < target:
            for i in range(mid, len(nums)):
                if nums[i] == target:
                    last = i
            for i in range(len(nums)-1, mid-1, -1):
                if nums[i] == target:
                    first = i
        elif nums[mid] > target:
            for i in range(mid, -1, -1):
                if nums[i] == target:
                    first = i
            for i in range(0, mid):
                if nums[i] == target:
                    last = i
        else:
            first = last = mid
            for i in range(mid, len(nums)):
                if nums[i] == target:
                    last = i
                else:
                    break
            for i in range(mid, -1, -1):
                if nums[i] == target:
                    first = i
                else:
                    break
        print(first, last)
        return [first, last] if nums[first] == target and nums[last] == target else [-1, -1]
    

if __name__ == '__main__':
    lst = [0,0,1,2,2]
    t = 0
    TestSolution.searchRange(lst, t)