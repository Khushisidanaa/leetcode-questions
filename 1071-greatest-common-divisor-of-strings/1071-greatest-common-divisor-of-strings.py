class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        
        a = len(str1)
        b = len(str2)
        g = self.gcd(a, b)

        g_word = str1[:g]
        
        return g_word