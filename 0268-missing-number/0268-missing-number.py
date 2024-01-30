class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)+1
        hashmap={}
        for index,value in enumerate(nums):
            hashmap[index]=value
             
        for i in range(0,n):
            if i not in nums:
                return i