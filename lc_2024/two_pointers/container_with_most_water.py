class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Intuition: 
        # two pointers -> left and right index
        # at minimum, 2 numbers exist
        # 1st CONDITION to calculate MAX_AREA -> DISTANCE * MIN(HEIGHT 1, HEIGHT 2)
        # EX 1. [1,0,0,0,0,0,0,0,7]
        # l = 0, r = 8
        # (r - l) = 8 * min(height[l], height[r])
        # 2nd CONDITION -> how we move the index?
        # move the lesser one? 

        # Initialize l, r and max_area -> constant space O(1)
        # while loop with l and r -> time complexity: O(n)
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        
if __name__ == "__main__":
    solution = Solution().maxArea
    assert(solution([1,8,6,2,5,4,8,3,7])==49)
    # Add your test cases here
    print("All test cases pass!")