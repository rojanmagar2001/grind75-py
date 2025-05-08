class Solution:
    def climbStairs(self, n: int) -> int:
        # This is a classic dynammic programming problem.
        # The number of ways to climb to step n is the sum of the number of ways to reach step n-1 and step n-2,
        # since you can take either 1 or 2 steps.
        # It follows the Fibonacci sequence:
        # ways(n) = ways(n - 1) + ways(n -2)

        # Optimal DP Solution (Buttom-Up, O(n) time, O(1) space)
        if n <= 2:
            return n

        a, b = 1, 2 # ways to climb to steps 1 and 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

        # Recursive Approach: Time Complexity: O(2^n), Space Complexity: O(n) (due to recursion stack)
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
