class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low!=high:
            if nums[high]<nums[low]:
                low+=1
            else:
                high-=1
        return nums[low]
            