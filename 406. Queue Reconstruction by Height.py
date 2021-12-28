


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
