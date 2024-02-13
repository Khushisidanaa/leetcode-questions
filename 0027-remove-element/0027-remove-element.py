class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        h = -1
        n=len(nums)
        for i in range(0,n):
            if nums[i]==val:
                h=i
                break
        if h!=-1:
            for j in range(h+1,n):
                if nums[j]!=val:
                    nums[j],nums[h]=nums[h],nums[j]
                    h+=1
           
        return len(nums) if h == -1 else len(nums[:h])
                
                
                
        