class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, d in enumerate(nums):
            complement = target - d
            if complement in h:
                return [i, h[complement]]
            
            h[d] = i
