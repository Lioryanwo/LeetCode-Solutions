class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0 
        n = len(s) - 1 
        start = 0
        k = 0
        result = ""

        if len(s) == 1:
            return s

        while i <= n:
            if s[n] == ' ':
                n -= 1
                continue

            start = n
            while n >= 0 and s[n] != ' ':
                n -= 1

            result += s[n+1:start+1] + ' '

        return result.strip()
