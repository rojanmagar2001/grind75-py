from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Pythonic Way
        mag_counts = Counter(magazine)

        for c in ransomNote:
            if c not in mag_counts or mag_counts[c] == 0:
                return False
            mag_counts[c] -= 1

        return True

        # Hash Map (Dict)
        ransome_note_char_dict = {}

        for ch in ransomNote:
            if ch in ransome_note_char_dict:
                ransome_note_char_dict[ch] += 1
            else:
                ransome_note_char_dict[ch] = 1

        for ch in magazine:
            if ch in ransome_note_char_dict:
                if ransome_note_char_dict[ch] > 0:
                    ransome_note_char_dict[ch] -= 1


        return all(count == 0 for count in ransome_note_char_dict.values())
