class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_right = 0
        l = 0
        n = len(height)
        r = n - 1
        water_count = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > max_left:
                    max_left = height[l]
                water_count += max_left - height[l]

                l += 1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                water_count += max_right - height[r]

                r -= 1
        return water_count