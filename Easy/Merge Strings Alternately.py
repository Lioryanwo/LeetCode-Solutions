class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merged = ""

        while i < len(word1) and j < len(word2):
            merged += word1[i]
            merged += word2[j]
            i += 1
            j += 1

        if i < len(word1):
            merged += word1[i:]

        if j < len(word2):
            merged += word2[j:]

        return merged
