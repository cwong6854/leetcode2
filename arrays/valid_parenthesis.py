class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # "[{([])}" -> false
        # [(]) -> false

        # must consider ordering of brackets, and must be enclosed by same type of bracket
        dic = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        order = []
        if len(s) == 1 or s[0] not in dic:
            return False
        for p in s:
            if p in dic:
                order.append(p)
            elif p not in dic and len(order) == 0:
                return False
            else:
                if p == dic[order[-1]]:
                    order.pop()
                else:
                    return False
        return True if len(order) == 0 else False

if __name__ == "__main__":
    x = "({[{()}]})"
    Solution.isValid(x)