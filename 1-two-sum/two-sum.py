class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
            n=nums[i]
            diff=target-n
            if diff in mp:
                return [mp[diff],i]
            mp[n]=i