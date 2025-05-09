# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]

        for num in nums[1:]:
            n ^= num  # Same number cancels out

        return n
