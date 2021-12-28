
The question wants to arrange the input queue such that the number of people infront of a person matches with heights of everybody else:
 nput: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
 
 Element in queue:
 #1 is placed at the begining so nobody has higher heigh than him
 #2 is placed there since nobody infront(hight 5) is taller
 #3 two people (hight 5 and 7) are infront of him
 #4 only (hight 7) is taller than him
 #5 4 people have hights higher
 #6 one person (hight 7) infront of him


"""        
 Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]       
        
def reconstructQueue(self, people):
    people.sort(key=lambda (h, k): (-h, k))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue
    
"""







class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(people)
        queue=[]
        for p in people:
            if p[1]==0:
                queue.append(p)
                people.remove(p)
                
        for p in people:
            if p[1]==len(queue):
                queue.append(p)
                people.remove(p)
        
        for _ in range(len(people)):        
            for p in people:
                n=0
                print(p)
                for q in queue:
                    if p[0]<=q[0]:
                        n+=1
                print(n)
                print(len(queue))
                
                if n==len(queue):
                    queue.append(p)
                    people.remove(p)
        
        return queue
