class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg=[]
        pos=[]
        for i in nums:
            if i<0:
                 neg.append(i)
            else:
                pos.append(i)
        for i in range(0,len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        return nums 
                
            