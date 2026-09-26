class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      res=set(nums)
      return True if len(res)<len(nums) else False
        