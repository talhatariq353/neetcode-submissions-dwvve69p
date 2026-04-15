class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        length = 0
        output = 0

        for i, num in enumerate(nums):
            if num-1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                output = max(length, output)
        
        return output

