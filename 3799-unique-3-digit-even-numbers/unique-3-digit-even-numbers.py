class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or i==k or j==k:
                        continue
                    if digits[k]%2!=0:
                        continue
                    if digits[i]==0:
                        continue
                    ans.add(100*digits[i]+10*digits[j]+digits[k])
        return len(ans)