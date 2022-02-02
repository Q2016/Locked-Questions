Question:
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). 
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height 
greater than or equal to hi. Reconstruct and return the queue that is represented by the input array people. The returned 
queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue 
(queue[0] is the person at the front of the queue).

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue. 


Solution: Sort

Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, 
therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth. Example: input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
It's not the most concise code, but I think it well explained the concept.

    def reconstructQueue(self, people):
        if not people: return []
        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []
        for i in xrange(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],
        height.sort() # here are different heights we have
        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])
        return res
  
