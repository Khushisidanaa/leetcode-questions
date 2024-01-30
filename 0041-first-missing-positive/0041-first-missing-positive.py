class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
    
    # Populate the hashmap
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # Start iterating from 1
        for i in range(1, len(nums) + 2):
            # Check if i is not in the hashmap or its count is 0
            if i not in hashmap or hashmap[i] == 0:
                return i
        