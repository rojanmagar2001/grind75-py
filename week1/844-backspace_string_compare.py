# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
#

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time & Space Complexity
        # Time: O(n + m) — where n is the length of s and m is the length of t
        # Space: O(n + m) for the stacks

        def build(s: str):
            stack = []

            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return stack

        return build(s) == build(t)

        # Alternative (Two Pointers, O(1) space):
