class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # find median of nums1
        m1 = (len(nums1)) // 2
        if len(nums1) % 2 == 0:
            m1_ = m1 - 1
            median1 = (nums1[m1] + nums1[m1_]) / 2
        else:
            median1 = nums1[m1]
        
        # find median of nums2
        m2 = (len(nums2)) // 2
        if len(nums2) % 2 == 0:
            m2_ = m2 - 1
            median2 = (nums2[m2] + nums2[m2_]) / 2
        else:
            median2 = nums2[m2]
        print(float(median1), float(median2))
        print((median1 + median2)/2)
        return (median1 + median2) / 2

if __name__ == "__main__":
    x = [1,2]
    y = [3,4]
    test = Solution()
    test.findMedianSortedArrays(x,y)