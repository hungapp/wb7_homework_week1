class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_to_list = list(s)
        pure_s_list = list(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))
        print(pure_s_list)
        for i in range(len(pure_s_list) // 2):
            if pure_s_list[i] != pure_s_list[-i - 1]:
                return False
        return True
