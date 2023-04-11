class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # merge sort
        # 1.) keep splitting the array in half --> recursive
        # [5,2,3,1] --> [5,2] [3,1]
        # [2, 5] [1, 3] 
        # [1, 2, 3, 5]

        #2.) [5,1,1,2,0,0] --> [5,1,1] [2,0,0]
        # [5,1] [1] | [2,0] [0]
        # [1,1,5] | [0,0,2] --> [0,0,1,1,2,5]


        #3.) [5,6,2,1,4]
        # [5,6] [2,1,4] 

        # def merging(lst1, lst2):
        #     lst = []
        #     for i in range(len(lst1)):
        #         curNum = lst1[i]
        #         j = i - 1
        #         while j >= 0 and lst1[j] > curNum:
        #             lst1[j+1] = lst1[j]
        #             j -= 1
        #         lst1[j+1] = curNum
        #     for i in range(len(lst2)):
        #         curNum = lst2[i]
        #         j = i - 1
        #         while j >= 0 and lst2[j] > curNum:
        #             lst2[j+1] = lst2[j]
        #             j -= 1
        #         lst2[j+1] = curNum

        #     l1 = l2 = 0
        #     while l1 < len(lst1) and l2 < len(lst2):
        #         if lst1[l1] < lst2[l2]:
        #             lst.append(lst1[l1])
        #             l1 += 1
        #         else:
        #             lst.append(lst2[l2])
        #             l2 += 1
        #     # print(lst)
        #     print(lst + lst1[l1:] + lst2[l2:])
        #     return lst + lst1[l1:] + lst2[l2:]

        # def split(lst1, lst2):
        #     if len(lst1) > 2 and len(lst2) > 2:
        #         split(lst1[len(lst1)//2:], lst1[:len(lst1)//2])
        #         split(lst2[len(lst2)//2:], lst2[:len(lst2)//2])
        #     return merging(lst1, lst2)
        
            

        # mid = len(nums) // 2
        # return split(nums[:mid], nums[mid:])

        def merging(lst, L, M, R):
            left, right = lst[L:M+1], lst[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    lst[i] = left[j]
                    j += 1
                else:
                    lst[i] = right[k]
                    k += 1
                i+=1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        def split(lst, l, r):
            if l == r:
                return lst
            m = (l + r) // 2
            split(lst, l, m)
            split(lst, m+1, r)
            merging(lst, l, m, r)
            return lst
        return split(nums, 0, len(nums) - 1)

    
if __name__ == "__main__":
    x = [5,2,3,1]
    w = Solution()
    print(w.sortArray(x))