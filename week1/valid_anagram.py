class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check: if the lengths are different, they can't ne anagrams
        if len(s) != len(t):
            return False

        # sorted_s = sorted(s) # -> O(nlogn) Easier Approach
        # sorted_t = sorted(t)

        # return sorted_s == sorted_t



        # Using Counter (most Pythonic)
        # from collections import Counter
        # return Counter(s) == Counter(t)
        #
        # char_count = {}
        # #  Count characters in first string
        # for char in s:
        #     char_count[char] = char_count.get(char, 0) + 1

        # # Decrease counts for second string
        # for char in t:
        #     if char not in char_count or char_count[char] == 0:
        #         return False
        #     char_count[char] -= 1

        # # All counts should be zero
        # return all(count == 0 for count in char_count.values())
        #

        distinct_chars = set(s)

        for ch in distinct_chars:
            if s.count(ch) != t.count(ch):
                return False

        return False
