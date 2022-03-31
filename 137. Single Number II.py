Question:
Given an array of integers, every element appears three times except for one. Find that single one. 
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


    
    
    
    
    
    
    
    
    
    
    
    
Solution:

    
    def singleNumber(self, nums): #(i like this one)
        
        return (sum(set(nums)) * 3 - sum(nums)) / 2
    

    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one
        

    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one
    

    def singleNumber(self, nums):

        return (collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys()[0]



    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two
    
    
    
    
# Time:  O(n)
# Space: O(1)    
