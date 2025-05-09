from typing import List

# 338. Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Clean and Efficient O(n) time solution without using any built-in bit counting functions. It uses dynamic programming
        # based on this observation:
        # The number of 1s in i is equal to the number of 1s in i // 2 (i.e., i >> 1) plus 1 if i is odd.
        ans = [0] * (n + 1)
        for i in range(0, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

        # Naive Approach O(n log n) solution
        # def count_ones(x: int):
        #     count = 0
        #     while x:
        #         count += x % 2
        #         x //= 2
        #     return count

        # return [count_ones(i) for i in range(0, n + 1)]



if __name__ == '__main__':
    solution = Solution()

    print(solution.countBits(25))
