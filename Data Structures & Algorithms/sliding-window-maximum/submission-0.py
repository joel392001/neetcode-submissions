import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []

        for r in range(len(nums)):
            while q and nums[r] > q[-1][0]:
                q.pop()
            q.append([nums[r],r])
            
            while q and q[0][1] <= r - k:
                q.popleft()

            if r >= k - 1:
                res.append(q[0][0])
            

        return res