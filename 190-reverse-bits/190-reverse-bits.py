class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        # traversing bits of 'n' from the right
        for i in range(32):
            rev = rev << 1
            rev += n & 1
            n = n >> 1

        return rev