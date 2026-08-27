class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Counter_T = Counter(t)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in Counter_T:
                Counter_T[s[i]] -= 1
                if Counter_T[s[i]] == 0:
                    del Counter_T[s[i]]
            else:
                return False
        return True