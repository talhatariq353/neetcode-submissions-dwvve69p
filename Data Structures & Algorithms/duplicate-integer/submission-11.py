class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = set()

        for i in nums:
            if i in already_seen:
                return True
            already_seen.add(i)
        
        return False

        