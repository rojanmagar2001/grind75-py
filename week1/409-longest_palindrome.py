from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Greedy Approach
        # Maximizing the palindrome by:
        # Adding all characters with even counts.
        # Adding the largest even part of any odd_count.
        # Plus one center character if any odd exists.
        # Time: O(n)
        # Space: O(1) — because only 52 possible letters (uppercase + lowercase)
        count = Counter(s)
        length = 0
        odd_found = False

        for char_count in count.values():
            length += (char_count // 2) * 2

            if char_count % 2 == 1:
                odd_found = True # We can place 1 odd character in the center

        return length + 1 if odd_found else length
