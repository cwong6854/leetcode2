class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Intuition:
        # two pointers -> left and right index
        # if left + right < target --> left + 1
        # elif left + right > target --> right - 1
        # else: return target

        # Time complexity: 
        # O(n) -> only visit each number once
        
        # Space complexity:
        # O(1) -> l and r are constant extra space
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l+1, r+1]
if __name__ == "__main__":
    solution = Solution().twoSum
    assert(solution([2,7,11,15], 9)==[1,2])
    # Add your test cases here
    print("All test cases pass!")