class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_len = min(len(s) for s in strs)
        prefix = ""
        
        for j in range(min_len):
            ch = strs[0][j]
            if all(s[j] == ch for s in strs):
                prefix += ch
            else:
                break
        return prefix

