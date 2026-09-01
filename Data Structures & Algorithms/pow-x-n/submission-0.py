class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1.0
            res=power(x,n//2)
            if n%2==0:
                return res*res
            else:
                return res*res*x
        if n<0:
            return 1/(power(x,-n))
        if x<0:
            return power(-x,n)
        else:
            return power(x,n)
        