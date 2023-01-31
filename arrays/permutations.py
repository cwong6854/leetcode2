class Solution(object):
    def permute(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            return [[nums[0]]]

        for i in range(len(nums)):
            fixed = nums[0]
            nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                res.append([fixed] + perm)
            nums.append(fixed)
        return res
            
if __name__ == "__main__":
    x = [1,2,3,4]
    a = Solution()
    a.permute(x)