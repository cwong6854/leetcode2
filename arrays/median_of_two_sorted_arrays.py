class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # [1,2,3,4,5,6,7,8]
        # [1,2,3,4,5]
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        # only perform binary search on smaller sorted array
        l, r = 0, len(A) - 1
        while True:
            # find midpoint for sorted arrays
            i = (l+r) // 2
            j = half - i - 2

            # find rightmost of left partitions and leftmost of right partitions
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j+1) < len(B) else float("infinity")
            # odd and even partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)*1.0 + min(Aright, Bright)*1.0) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

if __name__ == "__main__":
    x = [1,2]
    y = [3,4]
    test = Solution()
    test.findMedianSortedArrays(x,y)