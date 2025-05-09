# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) and strs[0][i] != word[i]:
                    return strs[0][:i]

        return strs[0]
