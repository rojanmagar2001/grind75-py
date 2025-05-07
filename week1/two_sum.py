from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, n in enumerate(nums):
            other_sum = target - n

            if other_sum in numsDict:
                return [numsDict[other_sum], i]

            if n not in numsDict:
                numsDict[n] = i

        return []
