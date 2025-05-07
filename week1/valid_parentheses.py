from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        mapped_brackets = {")": "(", "}": "{", "]": "["}

        stack: List[str] = list()

        for i in s:
            if (i == "{") or (i == "(") or (i == "["):
                stack.append(i)
            else:
                if len(stack) > 0:
                    if mapped_brackets[i] == stack.pop():
                        continue

                return False

        return len(stack) == 0
