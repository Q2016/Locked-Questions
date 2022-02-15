Question:
We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and 
the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, 
both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.    


Solution: Stack

A row of asteroids is stable if no further collisions will occur. After adding a new asteroid 
to the right, some more collisions may happen before it becomes stable again, and all of those 
collisions (if they happen) must occur right to left. This is the perfect situation for using a stack.

Say we have our answer as a stack with rightmost asteroid top, and a new asteroid comes in. If 
new is moving right (new > 0), or if top is moving left (top < 0), no collision occurs.

Otherwise, if abs(new) < abs(top), then the new asteroid will blow up; if abs(new) == abs(top) 
then both asteroids will blow up; and if abs(new) > abs(top), then the top asteroid will blow up 
(and possibly more asteroids will, so we should continue checking.)


class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
      
      
Complexity Analysis
Time Complexity: O(N), where N is the number of asteroids. Our stack pushes and pops each asteroid at most once.
Space Complexity: O(N). We use a stack to keep track of the intermediate results. 
In the worst case, the states do not evolve at the end, i.e. we need O(N) space where N is the number of input asteroids.

      
