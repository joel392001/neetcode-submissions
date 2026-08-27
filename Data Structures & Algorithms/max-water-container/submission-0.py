class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights) 
        r = n - 1
        maxi = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxi = max(maxi, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxi