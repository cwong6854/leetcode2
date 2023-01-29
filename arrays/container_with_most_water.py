class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        # first have to determine indices of height
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

if __name__ == "__main__":
    x = [1,2,4,3]
    Solution.maxArea(x)