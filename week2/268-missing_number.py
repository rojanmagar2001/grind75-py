# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Using sum of n numbers
        n = len(nums) # as it is from 0 to n we can ignore 0 
        expected_sum =  n * (n + 1) / 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum
