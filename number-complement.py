class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        power = 1
        while num:
            result += (num % 2 ^ 1) * power
            num >>= 1
            power <<= 1
        return result
