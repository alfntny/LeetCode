class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxA=0
        stack=[]

        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                ind,hts=stack.pop()
                maxA=max(maxA, hts*(i-ind))
                start=ind
            stack.append((start,h))
        for i,h in stack:
            maxA=max(maxA,h*(len(heights)-i))
        return maxA