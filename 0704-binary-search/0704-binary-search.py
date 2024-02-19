class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary(nums, low, high, target):
            while low<=high:
                mid=(low+high)/2
                if  nums[mid]== target:
                    return mid
                elif nums[mid]>target:
                    return binary(nums,low, mid-1, target)
                else:
                    return binary(nums,mid+1, high, target)
            else:
                return -1
        val=binary(nums, 0, len(nums)-1, target)
        return val
                    