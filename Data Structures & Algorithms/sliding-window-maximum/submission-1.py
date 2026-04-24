class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        r = 0
        res = []

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if r - l + 1 == k:
                res.append(nums[q[0]])
                if l == q[0]:
                    q.popleft()
                l += 1

            r += 1

        return res