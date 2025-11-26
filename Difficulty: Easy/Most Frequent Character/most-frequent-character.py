class Solution:
    def getMaxOccurringChar(self, s):
        freq = {}

        # Count frequency of each character
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Sort dictionary by key (character)
        freq = dict(sorted(freq.items()))

        # Find the maximum frequency
        max_count = max(freq.values())

        # Return the character with maximum count
        # Alphabetically smallest will be returned first because dict is sorted
        for key, val in freq.items():
            if val == max_count:
                return key
