class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0

        for i in range(32):

            # Step 1: extract the last (rightmost) bit of n
            bit = n & 1

            # Step 2: shift result left to make room for new bit
            #         then OR the new bit in
            result = (result << 1) | bit

            # Step 3: shift n right to look at next bit
            n >>= 1

        return result