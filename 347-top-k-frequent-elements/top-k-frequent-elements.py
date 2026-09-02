class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        s={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in s:
                s[nums[i]]+=1
            else:
                s[nums[i]]=1
        sorted_items = sorted(
            s.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [key for key, value in sorted_items[:k]]