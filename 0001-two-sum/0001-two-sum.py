class Solution:
    
    @staticmethod
    def pair_elements_with_indices(nums):
        return [(num, i) for i, num in enumerate(nums)]

    @staticmethod
    def sort_by_value(paired_list):
        return sorted(paired_list, key=lambda x: x[0])

    def twoSum(self, nums, target):
        # Pair each element with its index and sort by the element value
        nums_with_indices = Solution.sort_by_value(Solution.pair_elements_with_indices(nums))
        
        left, right = 0, len(nums_with_indices) - 1
        while left < right:
            current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if current_sum == target:
                # Return the original indices of the two numbers
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
