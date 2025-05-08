from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distint_nums = set(nums)

        return len(distint_nums) == len(nums)
