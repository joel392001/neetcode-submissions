class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        max_freq = 0
        res = 0
        l = 0
        n = len(s)

        for r in range(n):
            seen[s[r]] += 1
            max_freq = max(max_freq, seen[s[r]])

            while (r - l + 1) - k > max_freq:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        return res
             