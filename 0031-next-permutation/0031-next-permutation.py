class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        # Find the first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # Find the element that is just larger than nums[i]
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the segment from i+1 onwards
        nums[i+1:] = nums[i+1:][::-1]
        return nums
            
        
#         flag = False
#         i = n=len(nums)-1
#         while i>=0:
#             if nums[i]>nums[i-1]:
#                 k=i-1
#                 flag = True
#         max=nums[k]
#         for i in range(k,n+1):
#             if nums[i]< max and nums[i]>nums[k]:
#                 max=nums[i]
#             elif nums[i]> nums[k]:
#                 max= nums[i]
#         nums[k], nums[max] = nums[max], nums[k]
       
#         if k < n:
#             # Reverse the segment from k+1 to the end
#             nums[k+1:] = nums[k+1:][::-1]
#         if flag == False:
#             nums=nums[::-1]
#         return nums
           
    
      
                    
            