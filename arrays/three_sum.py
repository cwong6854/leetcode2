class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort nums -> O(N)
        nums.sort()
        triplets = []
        # [-1, 0, 1, 2, -1, -4] --> [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                if threeSum > 0:
                    r -= 1
                if threeSum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    if nums[l] == nums[l-1]:
                        l += 1

        return triplets
    
if __name__ == "__main__":
    x = [0,0,0,0]
    w = Solution()
    print(w.threeSum(x))