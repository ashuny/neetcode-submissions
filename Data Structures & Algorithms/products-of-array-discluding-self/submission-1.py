class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        
        suffix = 1 
        for j in reversed(range(len(nums))):
            res[j] *= suffix
            suffix *= nums[j]
        
        return res