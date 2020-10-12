class Solution:
    def binaryGap(self, n: int) -> int:
        last_1_idx = None
        res = 0
        for i in range(32):
            if (n >> i) & 1:
                if last_1_idx is not None: 
                    res = max(res, i - last_1_idx)
                    print(res)
                last_1_idx = i
        return res
