Question:
Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, 
the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" 
if there are infinite solutions for the equation. If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

Example 1:
Input: equation = "x+5-3+x=6+x-2", Output: "x=2"
    
Solution: Regix
    
    def solveEquation(self, equation):
        a, b, side = 0, 0, 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                a += side * int(sign + '1') * int(num or 1)
            elif num:
                b -= side * int(sign + num)
        return 'x=%d' % (b / a) if a else 'No solution' if b else 'Infinite solutions'
