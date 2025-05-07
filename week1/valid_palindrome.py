import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # -> O(n)

        reversed_s = clean_s[::-1] # -> O(n)

        return clean_s == reversed_s
