class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        else:
            s = set()
            l = 0
            for n in nums:
                s.add(n)
                l += 1
                if l != len(s):
                    return True
            return False