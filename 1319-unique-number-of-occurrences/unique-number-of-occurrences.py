class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s={}
        for i in arr:
            if i not in s:
                s[i]=1
            else:
                s[i]=s[i]+1
        res=[]
        for i in s.values():
            if i not in res:
                res.append(i)
            else:
                return False
        return True