class Solution:
    def minEatingSpeed(self, piles: List[int], k: int) -> int:
        l = 1
        h = max(piles)

        while l <= h:
            mid = (l + h) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)

            if hours <= k:
                h = mid - 1
            else:
                l = mid + 1
        return l