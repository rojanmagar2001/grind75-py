# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Brute Force Approach
        # Time: O(n)
        # Space: O(1)
        for i in range(1, n+1):
            if isBadVersion(i):
                return i

        # Binary Search Approach
        # Time: O(log n)
        # Space: O(1)
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid # Mid might be the first bad version
            else:
                left = mid + 1 # first bad version is after mid

        return left # or right (both are equal here)
