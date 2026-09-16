class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0
        res=[[]]
        for i in nums:
            new=[]
            for lst in res:
                new.append(lst+[i])
            res+=new
        for i in res:
            if len(i)==0:
                continue
            else:
                sm=0
                for j in i:
                    sm^=j
                s=s+sm
        return s