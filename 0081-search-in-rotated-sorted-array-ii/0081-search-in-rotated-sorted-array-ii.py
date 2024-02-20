class Solution:
    def search(self, nums, target) :
        flag=False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left] == nums[right]:
                left+=1
                right-=1
            else:

                # Check if left half is sorted
                if nums[left] <= nums[mid]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                # Otherwise, right half is sorted
                else:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

        return flag