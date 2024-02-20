class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            # Determine if the mid element is in the left or right sorted subarray
            if nums[mid] >= nums[low]:  # Mid is in the left sorted subarray
                if nums[low] <= target < nums[mid]:  # Target is in the left subarray
                    high = mid - 1
                else:  # Target is in the right subarray
                    low = mid + 1
            else:  # Mid is in the right sorted subarray
                if nums[mid] < target <= nums[high]:  # Target is in the right subarray
                    low = mid + 1
                else:  # Target is in the left subarray
                    high = mid - 1

        return -1
