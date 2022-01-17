Approach 1: Greedy (Two Pointer)
Intuition

If the heaviest person can share a boat with the lightest person, then do so. Otherwise, 
the heaviest person can't pair with anyone, so they get their own boat.

The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.

Algorithm

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
