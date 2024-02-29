class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        l=0
        r=len(s)-1
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                s= s[0:l]+s[r]+s[l+1:r]+s[l]+s[r+1:]
                l+=1
                r-=1
            else: 
                if s[l] not in vowels:
                    l+=1
                if s[r] not in vowels: 
                    r-=1    
        return s
        