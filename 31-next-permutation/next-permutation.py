class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=len(nums)-2
        p=0
        while r>=0 and nums[r]>=nums[r+1]:
            r-=1
        if r == -1:
            nums.reverse()
            return
        p=r
        j=len(nums)-1
        while nums[j]<=nums[p]:
            j-=1
        nums[j],nums[p]=nums[p],nums[j]
        left=p+1
        right=len(nums)-1
        while left<=right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
