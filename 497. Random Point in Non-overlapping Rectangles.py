Question:
You are given an array of non-overlapping rectangles rects[i] = [ai, bi, xi, yi] with 
(ai, bi) bottom-left corner (xi, yi) top-right corner point. 
-A point on the perimeter of a rectangle is included in the space covered by the rectangle.
-Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.    
Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. 














Solution: Extention of problem 528. Random Pick with Weight
The idea is simple;

Choose a rect, then choose a point inside it.
The bigger the rectangle, the higher the probability of it getting chosen
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        
        # I am more of a list comprehensions guy, but if you prefer to
        # put more effort with the keyboard, here's an unrolled version.
        
        # self.weights = []
        # for rect in rects:
        #     x1, y1, x2, y2 = rect
        #     area = (x2-x1+1)*(y2-y1+1)
        #     self.weights.append(area)
        
        self.weights = [(x2-x1+1)*(y2-y1+1) for x1, y1, x2, y2 in rects]
        
            
        # library functions are always faster
        # it beats the runtime of using an extra variable 
        # to calculate sum_of_weights in the loop above
        # even if that means, we have to iterate once more.
        # Such is the world of python :D
        sum_of_weights = sum(self.weights)
        
        self.weights = [x/sum_of_weights for x in self.weights]
            

    def pick(self) -> List[int]:
        
        # random.choices returns a list, we extract the first (and only) element.
        rect = random.choices(population=self.rects, weights=self.weights, k=1)[0]  

        x1, y1, x2, y2 = rect  # tuple unpacking
        
        rnd_x = random.randint(x1, x2)
        rnd_y = random.randint(y1, y2)
        return [rnd_x, rnd_y]
        


Remark: Note, that there is solution with O(1) time/space complexity for pick, using smart mathematical trick, 
see my solution of problem 528: https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation
    
