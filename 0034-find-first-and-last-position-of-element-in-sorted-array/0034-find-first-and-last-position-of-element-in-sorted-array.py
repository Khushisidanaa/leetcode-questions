class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def firstsolution(nums,low,high,target):
            first=-1
            while low<=high :
                mid=(low+high)/2
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]<=target:
                    low=mid+1
                else:
                    high=mid-1
            return first
            
            
        
        def lastelement(nums,low,high,target):
            last=-1
            while low<=high  :
                mid=(low+high)/2
                if nums[mid]==target:
                   
                    last=mid
                    low=mid+1
                elif nums[mid]<=target:
                    low=mid+1   
                else:
                    high=mid-1
           
            return last 
       
                    
        return firstsolution(nums,0,len(nums)-1,target),lastelement(nums,0,len(nums)-1,target)