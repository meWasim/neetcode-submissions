class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        res=[]
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
        return res
        