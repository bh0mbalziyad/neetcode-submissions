class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = ""

        first_word = strs[0]
        for i in range(len(first_word)):
            for s in strs:
                if len(s) == i or s[i] != first_word[i]:
                    return res
            res += first_word[i]

        return res