class Solution(object):
    def topKFrequent(self, nums, k):
        # Intuition
        # iterate through array, track count of elements with hashmap, 
        # then sort, return k most frequent elements
        # with log n -> need to find sorting algorithm
        
        # Time Complexity
        # O (n * log N) -> iterate through nums -> O(N), sort values, doesn't sort items that are already in place -> O(log n)

        # Space Complexity
        # O(n)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_el = {}
        for n in nums:
            freq_el[n] = freq_el.get(n, 0) + 1
        return [x[0] for x in sorted(freq_el.items(), key=lambda x: x[1], reverse=True)][:k]
if __name__ == "__main__":
    solution = Solution().topKFrequent
    assert(solution([3,3,3,3,2,1], k=2))==[3,2]
    # Add your test cases here
    print("All test cases pass!")