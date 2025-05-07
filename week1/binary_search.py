from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #  Initialize the left and right pointers
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Calculate the middle index
            mid = left + (left - right) // 2

            # Check if we found the target
            if nums[mid] == target:
                return mid

            # if target is less than the middle element, search the left half:
            if nums[mid] > target:
                right = mid - 1

            # if target is greater than the middle element, search the right half.
            else:
                left = mid + 1

        return -1
