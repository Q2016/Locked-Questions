Question:
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses. If multiple answers are possible, 
return any of them. It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"    
    
    
Solution: Stack


Use stack to store a remainder while doing the division so that whenever a same remainder comes up, 
we know there is a repeating fractional part.


def fractionToDecimal(self, numerator, denominator):
    
    n, remainder = divmod(abs(numerator), abs(denominator))
    sign = '-' if numerator*denominator < 0 else ''
    result = [sign+str(n), '.']
    stack = []
    
    while remainder not in stack:
        stack.append(remainder)
        n, remainder = divmod(remainder*10, abs(denominator))
        result.append(str(n))

    idx = stack.index(remainder)
    result.insert(idx+2, '(')
    result.append(')')
    return ''.join(result).replace('(0)', '').rstrip('.')
