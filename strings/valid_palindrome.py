class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                letters += c.lower()
        l, r = 0, len(letters) - 1
        while l < r:
            if letters[l] != letters[r]:
                return False
            l += 1
            r -= 1
        return True
    
if __name__ == "__main__":
    x="0P"
    w = Solution()
    w.isPalindrome(x)