class Solution(object):
    def sortColors(self, nums):
        t=len(nums)-1
        z=0
        i= 0
        while t>=i:
            if nums[i]==0:
                nums[z], nums[i] = nums[i], nums[z]
                z+=1
                i+=1
            elif nums[i]==2:
                nums[i], nums[t] = nums[t], nums[i]
                t-=1
            else:
                i+=1
        