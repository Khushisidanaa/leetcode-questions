class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum =( n*(n+1))/2
        total=0
        for i in nums:
            total+=i
        return (sum-total)