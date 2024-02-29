class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num=len(flowerbed)
        count=0
        if num==1:
            if flowerbed[0]==0:
                count+=1
        else:
            for i in range(num):
                if i==0:
                    if flowerbed[i]==0 and flowerbed[i+1]==0:
                        count+=1
                        flowerbed[i] = 1
                elif i==num-1:
                     if flowerbed[i]==0 and flowerbed[i-1]==0:
                        count+=1
                        flowerbed[i] = 1 
                elif flowerbed[i+1]!=1 and flowerbed[i-1]!=1 and flowerbed[i]==0:
                    count+=1
                    flowerbed[i]=1

        if count>=n:
            return True
        else:
            return False

        
        