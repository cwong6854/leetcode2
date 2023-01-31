class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search
        # two cases:
        # rotated array or fully rotated

        # 1.) Fully Rotated Array Case
        # if fully rotated, we can check left pointer and if its less than right pointer


        # 2.) Rotated Array Case
        # find midpoint, if mid point is greater/equal to left pointer, search right side
        # otherwise, search left side

        #Runtime: O(log n)

        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return res

if __name__ == "__main__":
    x = [5,6,1,2,3,4]
    Solution.findMin(x)