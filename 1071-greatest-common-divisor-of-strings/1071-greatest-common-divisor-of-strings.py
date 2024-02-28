class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0]:
            return ""
        
        a = len(str1)
        b = len(str2)
        g = self.gcd(a, b)

        g_word = str1[:g]
        if str1.count(g_word) == a // g and str2.count(g_word) == b // g:
            return g_word
        return ""