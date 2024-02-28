class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxc=max(candies)
        
        return [num + extraCandies >= maxc for num in candies]
        
        