class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1,t1={},{}
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]]=0
            if t[i] not in t1:
                t1[t[i]]=0
            t1[t[i]]+=1
            s1[s[i]]+=1

        if s1==t1:
            return True  
        return False