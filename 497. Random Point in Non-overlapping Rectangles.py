Question:
You are given an array of non-overlapping rectangles rects[i] = [ai, bi, xi, yi] with 
(ai, bi) bottom-left corner (xi, yi) top-right corner point. 
-A point on the perimeter of a rectangle is included in the space covered by the rectangle.
-Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.    
Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. 














Solution: Extention of problem 528. Random Pick with Weight
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/discuss/805232/Python-Short-solution-with-binary-search-explained

Here we have several rectangles and we need to choose point from these rectangles. We can do it in two steps: Choose rectangle. Note, that 
the bigger number of points in these rectangle the more should be our changes. Imagine, we have two rectangles with 10 and 6 points. Then we 
need to choose first rectangle with probability 10/16 and second with probability 6/16. Choose point inside this rectangle. We need to choose 
coordinate x and coordinate y uniformly. When we initailze we count weights as (x2-x1+1)*(y2-y1+1) because we also need to use boundary. 
Then we evaluate cumulative sums and normalize.
For pick function, we use binary search to find the right place, using uniform distribution from [0,1] and then we use uniform discrete 
distribution to choose coordinates x and y.


class Solution:
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]

    
    
Complexity: 
Time and space complexity of __init__ is O(n), where n is number of rectangles. 
Time complexity of pick is O(log n), because we use binary search. 
Space complexity of pick is O(1).

Remark: Note, that there is solution with O(1) time/space complexity for pick, using smart mathematical trick, 
see my solution of problem 528: https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation
    
