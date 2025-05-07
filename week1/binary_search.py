from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #  Initialize the left and right pointers
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Get the mid point
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # if target is less than mid, search through left half
            if nums[mid] > target:
                right = mid - 1

            # else, search through right half
            else:
                left = mid + 1

        return -1
