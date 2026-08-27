class Solution:
    def minWindow(self, s: str, t: str) -> str:
        Counter_t = Counter(t)

        window = defaultdict(int)
        need = len(Counter_t)
        have = 0
        longest = float("inf")
        res = ""
        l = 0

        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in Counter_t and window[s[r]] == Counter_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < longest:
                    longest = r - l + 1
                    res = s[l:r + 1]

                window[s[l]] -= 1
                if s[l] in Counter_t and Counter_t[s[l]] > window[s[l]]:
                    have -= 1 
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return res



