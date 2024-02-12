import numpy as np
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0]) 
        r=[]
        c=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        for p in range(len(r)):
            i=r[p]
            j=c[p]
            for k in range(n):
                matrix[i][k]=0
            for l in range(m):
                matrix[l][j]=0
        return matrix
                    