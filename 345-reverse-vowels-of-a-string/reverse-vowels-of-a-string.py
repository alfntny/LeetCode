class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        ans=""
        for i in s:
            if i in 'aeiouAEIOU':
                vowel.append(i)
        for i in s:
            if i not in 'aeiouAEIOU':
                ans=ans+i
            else:
                ans=ans+vowel[-1]
                vowel.pop()
        return ans