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

# original approach
    def binaryGap(self, n: int) -> int:
    n_binary = bin(n)
            i = 2
            last_1_index = i
            max_distance = 0
            while i < len(n_binary):
                if n_binary[i] == '1':
                    max_distance = max(max_distance, i - last_1_index)
                    last_1_index = i
                i += 1
            return max_distance