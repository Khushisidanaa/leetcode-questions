class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        """
        min=0
        max=j=1
        impdifference=0
        while j<len(prices):
            if prices[j]<prices[min]:
                min=j
                
            else:
                difference = prices[j]-prices[min]
                if difference>impdifference:
                    impdifference = difference 
            j+=1

            
        return impdifference
        
        

         
    
     