# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Time & Space:
        # Time: O(n) — single pass.
        #
        # Space: O(1) — in-place swaps only.
        # Traverse the array with right.
        #
        # Whenever nums[right] is non-zero:
        #
        # Swap it with nums[left].
        #
        # Increment left to point to the next position for a non-zero.
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1


        # Two Cursor Approach O(n + m) m is the number of zeros
        insert_pos = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
               
     
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
