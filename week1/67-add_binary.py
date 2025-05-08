class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Naive Approach
        # Time: O(n)
        # Space: O(1)
        # max_len = max(len(a), len(b))

        # a = a.zfill(max_len)
        # b = b.zfill(max_len)

        # sum = ''
        # carry = 0

        # for i in range(max_len - 1, -1, -1):
        #     r = carry

        #     r += 1 if a[i] == '1' else 0
        #     r += 1 if b[i] == '1' else 0

        #     sum = ('1' if r % 2 == 1 else '0') + sum

        #     # Compute the carry
        #     carry = 0 if r < 2 else 1

        # if carry != 0:
        #     sum = '1' + sum

        # return sum
        #

        # Using Pyton builtin function bin and int
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]
