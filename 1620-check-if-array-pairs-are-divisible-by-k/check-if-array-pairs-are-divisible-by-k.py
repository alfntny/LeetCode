class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        d={}
        for i in arr:
            rem=i%k
            if rem not in d:
                d[rem]=0
            
            d[rem]+=1
        for rem in d:
            pair=(k-rem)%k

            if pair not in d:
                return False
            if rem == pair:
                if d[rem] % 2 != 0:
                    return False
            elif d[rem] != d[pair]:
                return False
        return True