class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 0;
        # while  i< len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)
        #two pointer
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1