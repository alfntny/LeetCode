class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=float('-inf')
        curr=0
        for i in nums:
            curr=curr+i
            maxs=max(maxs,curr)
            if curr<0:
                curr=0
        return maxs