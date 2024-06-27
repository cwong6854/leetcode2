class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Intuition:
        # input has spaces and uppercase, but palindrome requires lowercase
        # given string input -> take out all uppercase and spaces
        # two pointers -> have left and right index:
        # - if equal, continue | else -> return false
        # ANOTHER CASE: 
        # ".s." -> . is printable ASCII character

        #check if character is a letter first -> add as lowercase
        # then check if is numeric as well
        # create new string from s
        # REMOVE ALL non-alphanumeric chars
        newS = ""
        for char in s:
            # check if char is printable ASCII characters
            if char != " ":
                if char.isalpha():
                    newS += char.lower()
                if char.isnumeric():
                    newS += char
        l, r = 0, len(newS) - 1
        while (l < r):
            if newS[l] != newS[r]:
                return False
            l += 1
            r -= 1
        return True
if __name__ == "__main__":
    solution = Solution().isPalindrome
    assert(solution("A man, a plan, a canal: Panama")==True)
    # Add your test cases here
    print("All test cases pass!")