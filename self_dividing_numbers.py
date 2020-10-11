class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        if not left:
            return res
        for n in range(left, right+1):
            if self.self_divided(n):
                res.append(n)
        return res
    
    def self_divided(self, num):
        for d in str(num):
            if d == '0' or num % int(d) != 0:
                return False
        return True
