class TestSolution(object):
    def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = [word]
            else:
                groups[sorted_word].append(word)
        return [groups[i] for i in groups]
        # groups = {}
        # groups[strs[0]] = [strs[0]]
        # grouped = False
        # for word in strs[1:]:
        #     for g in groups.copy():
        #         w = list(g)
        #         tmp = list(word)
        #         for s in word:
        #             if s in w:
        #                 w.remove(s)
        #                 tmp.remove(s)
        #         if len(w) == 0 and len(tmp) == 0:
        #             groups[g].append(word)
        #             grouped = True
        #     if grouped == False:
        #         groups[word] = [word]
        #     else:
        #         grouped = False
        # return [groups[i] for i in groups]


if __name__ == "__main__":
    x = ["eat","tea","tan","ate","nat","bat"]
    TestSolution.groupAnagrams(x)
