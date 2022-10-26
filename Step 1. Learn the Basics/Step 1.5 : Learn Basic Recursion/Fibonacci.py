# [[1, 1], [1, 2]]
# [[1, 2], [2, 3]]
# [[2, 3], [3, 5]]
# [[3, 5], [5, 8]]
# [[5, 8], [8, 13]]
# [[8, 13], [13, 21]]
# [[13, 21], [21, 34]]
# [[21, 34], [34, 55]]
# [[34, 55], [55, 89]]
# [[55, 89], [89, 144]]

# Fibonacci - O(logN) Time complexity

class Solution:
    def multiply(a,b):
        c=[[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] = c[i][j] + (a[i][k]*b[k][j])
        return c
    def coef(a,n):
        res = [[1,0],[0,1]]
        while(n>0):
            if(n%2==1):
                res=Solution.multiply(res,a)
            a=Solution.multiply(a,a)
            n=n//2
        return res
    def printFibb(self,n):
        a=[[0,1],[1,1]]
        print(Solution.coef(a,n)[1][0])
