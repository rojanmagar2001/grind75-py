# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapped_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i, rchar in enumerate(s):
            if (len(s) > i + 1) and (roman_mapped_integer[rchar] < roman_mapped_integer[s[i + 1]]): # This is the case for IV where less means minus
                result -= roman_mapped_integer[rchar]
            else:
                result += roman_mapped_integer[rchar]

        return result
