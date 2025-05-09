# 191. Number of 1 Bits

# Given a positive integer n, write a function that returns
# the number of in its binary representation (also known as the Hamming weight).

from collections import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Using Bit Wise Operation
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

        # Naive Way
        bin_reps = bin(n)

        bits_count = Counter(bin_reps)

        return bits_count["1"]
