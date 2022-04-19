Question:
Implement pow(x, n), which calculates x raised to the power n.    
















Solution: Recursive, Iterative

If we have very small value of x we can directly return 0, the smallest value of float is 1.175494 × 10^(-38).    
    
Recursive:

    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

Iterative:

    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
    
since you're dividing N by 2 every iteration that's why it is O(Log N). However, since N is a fixed number of bits (32) you could 
view it as O(1) where the maximum number iterations is 32. Hope this helps.


