# 190. Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
# 1. Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be 
# given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is 
# the same, whether it is signed or unsigned.
# 2. In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input 
# represents the signed integer -3 and the output represents the signed integer -1073741825.


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n & 1            # get the last bit
            result = (result << 1) | bit  # shift result left and add bit
            n >>= 1                # shift n right
        return result 
