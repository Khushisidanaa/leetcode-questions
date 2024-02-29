class Solution:
    def reverseWords(self, s: str) -> str:
        str1=s.split()
        l=0
        r=len(str1)-1
        if len(str1)==1:
            return s.strip()
        while l<=r:
            str1[l],str1[r] = str1[r], str1[l]
            l+=1
            r-=1
        return ' '.join(str1)