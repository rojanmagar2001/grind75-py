# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass

    def isPalindromeUsingString(self, x: int) -> bool:
        if x < 0: # negative numer can never be palindrome
            return False

        x_str = str(x) 

        return x_str == x_str[::-1]

    def isPalindromeWithoutUsingString(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0 or x % 10 == 0: # negative numer can never be palindrome
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # If even length, both halves will be equal
        # If odd, drop the middle digit in reversed_half using //
        return x == reversed_half or x == reversed_half // 10 # Ignoring if there is odd number


