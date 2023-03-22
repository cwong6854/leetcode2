class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    res += 1
                l -= 1
                r += 1
            l, r = i, i
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    res += 1
                l -= 1
                r += 1
        return res
                
if __name__ == "__main__":
    x = "aaa"
    w = Solution()
    w.countSubstrings(x)





        

