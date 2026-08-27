class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # start_idx, height
        max_area = 0

        for i,height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
               start_idx, h = stack.pop()
               max_area = max(max_area, (i - start_idx) * h)
               start = start_idx
            stack.append((start,height))

        while stack:
            i, height = stack.pop()
            max_area = max(max_area, (len(heights) - i) * height)
            
        return max_area