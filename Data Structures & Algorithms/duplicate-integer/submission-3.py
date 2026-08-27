class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        n = len(nums)
        return True if len(num) < n else False