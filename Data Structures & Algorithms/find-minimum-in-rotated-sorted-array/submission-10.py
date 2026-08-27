class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [l 3,4,m 5,6,1,2 h]
        l = 0
        h = len(nums) - 1

        while l < h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[l]