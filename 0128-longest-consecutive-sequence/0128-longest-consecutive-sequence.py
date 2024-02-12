class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={}
        for i in nums:
            hash[i] = 'True'  
        maxcount=0
       
        for i in hash:
            if i-1 not in hash:
                count=1
                j=1
                while i+j in hash:
                        count+=1
                        j+=1
                if count>maxcount:
                    maxcount=count
        return maxcount
                
            
            