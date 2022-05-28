Question:
Numbers can be regarded as product of its factors. For example, 8 = 2 x 2 x 2; = 2 x 4. Write a function that takes an 
integer n and return all possible combinations of its factors.

Examples: 
input: 12
output:[[2, 6],[2, 2, 3],[3, 4]]  

    
    
    
    
    
    
    
    
    
    
Solution: (Backtracking, it has similarity to the prime factors)    

class Solution(object):

    def getFactors(self, n):

        if n == 1:
            return []
        
        index=2
        product=1
        temp=[]
        result=[]
        
        def backtrack(temp, product, index):
            if product>n:
                return
            
            if product==n:
                result.append([temp])
        
            for i in range(index, n/product):
                if n % i == 0 and i!=n :
                    temp.append(i)
                    backtrack(temp, product * i, i)
                    temp.pop()
                    
        backtrack(temp, product, index)
        
        return result
