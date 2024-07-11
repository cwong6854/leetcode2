class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Intuition:
        # Cannot sell price day before a buy price day
        # for loop through the prices array O(N)
        # have an index representing buy price -> day 1
        # if there's profit, store that profit and compare with the maximum profit
        # CONDITION TO MOVE INDEX FOR BUY PRICE
        # ---> if buy price is less than sell price

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res, b = 0, 0
        for i in range(len(prices)): # O(n)
            if b == i:
                continue
            profit = prices[i] - prices[b]
            if profit < 0: # if buy price less than sell price, set buy price to sell price day
                b = i
            else:
                res = max(res, profit)
        return res
if __name__ == "__main__":
    solution = Solution().maxProfit
    assert(solution([7,1,5,3,6,4])==5)
    # Add your test cases here
    print("All test cases pass!")