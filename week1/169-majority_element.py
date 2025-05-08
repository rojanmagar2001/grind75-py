from typing import Counter, List

class Solution:
    def majorityElement(self, nums: List[int]) -> int | None:
        # 2, 2, 1, 1, 1, 2, 2
        #
        # Boyer-Moore Voting Algorithm
        # Time: O(n)
        # Space: O(1)
        # 🧠 How it works:
        # It cancels out different elements against each other. The majority element survives the elimination process.
        count = 0
        candidate: int | None = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


        # HashMap / Counter (Simple)
        # Time: O(n)
        # Space: O(n)
        # Simple but not optimal for space
        counts = Counter(nums)
        return max(counts, key=counts.get)
