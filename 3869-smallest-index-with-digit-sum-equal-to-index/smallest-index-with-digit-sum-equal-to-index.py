class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def integer(n):
            s=str(n)
            sm=0
            for i in range(len(s)):
                sm=sm+int(s[i])
            return sm
        l=[]
        for i in range(len(nums)):
            if i==integer(nums[i]):
                l.append(i)
        return min(l) if l else  -1