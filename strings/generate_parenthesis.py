class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # At each recursion, we check if left is greater than 0, then input "("
        # Otherwise, we check if right is greater than 0 and if right is greater than left
        # left MUST ALWAYS be less than right, otherwise it is not valid
        res = []
        def generate(left, right, par):
            if left == 0 and right == 0 and par not in res:
                res.append(par)
            if left > 0:
                generate(left-1, right, par + "(")
            if right > 0 and left < right:
                generate(left, right-1, par + ")")
        generate(n, n, "")
        return res
            
if __name__ == "__main__":
    n = 3
    w = Solution()
    print(w.generateParenthesis(n))