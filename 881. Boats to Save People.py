Question:
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can 
carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)    

    
    
    
    
    
    
    
    
Solution: Greedy (Two Pointer)

If the heaviest person can share a boat with the lightest person, then do so. Otherwise, 
the heaviest person can't pair with anyone, so they get their own boat.
The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.
Let people[i] to the currently lightest person, and people[j] to the heaviest.
Then, as described above, if the heaviest person can share a boat with the lightest person 
(if people[j] + people[i] <= limit) then do so; otherwise, the heaviest person sits in their own boat.


class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
