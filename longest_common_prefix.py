class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        result = ''
        if not strs:
            return result
        first_word = strs[0]
        for i, c in enumerate(first_word):
            is_common = True
            for other_word in strs[1:]:
                if i > len(other_word) - 1  or c != other_word[i]:
                    is_common = False
                    break
            if is_common:
                result += c
            else:
                break
        return result
