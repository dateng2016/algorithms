class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = 1 & (n >> i)
            res |= bit << (31 - i)
        return res

