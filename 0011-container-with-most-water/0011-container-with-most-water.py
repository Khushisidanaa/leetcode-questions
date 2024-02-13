class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         max=0
#         l=0
#         r=len(height)-1
        
#         while l<r:
#             diff=r-l
#             small= min(height[l],height[r])
#             val=diff*small
#             if val<max: 
#                 r-=1
#             else:
#                 l+=1
#                 max=val
        # return max
    
        maxi=0
        l=0
        r=len(height)-1
        while l<r:
            diff=r-l
            small= min(height[l],height[r])
            val=diff*small
            if val>maxi:
                maxi=val

            if height[l]>=height[r]: 
                r-=1
            else:
                l+=1

        return maxi

        