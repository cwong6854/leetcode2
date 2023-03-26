class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # if len(nums) <= 1:
        #     return nums
        # for i in range(1, len(nums)):
        #     currNum = nums[i]
        #     for j in range(i-1, -1, -1):
        #         prevNum = nums[j]
        #         if currNum < prevNum:
        #             nums[j] = currNum
        #             nums[i] = prevNum
        #             currNum = prevNum
        # return nums
        if len(nums) <= 1:
            return nums
        for i in range(1, len(nums)):
            curr = nums[i]
            j = i - 1
            while j >= 0 and curr < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j + 1] = curr
        return nums
    
if __name__ == "__main__":
    x = [5,2,3,1]
    w = Solution()
    print(w.sortArray(x))