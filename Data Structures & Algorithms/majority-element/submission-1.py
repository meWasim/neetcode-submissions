class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}

        for num in nums:
           if num not in res:
                res[num]= nums.count(num)
        return max(res,key=res.get)
