Question:
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, 
return the earliest time slot that works for both of them and is of duration duration.

Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]


Solution: Sort
  
Time O (nlogn) 
Space O (1)
  
  
      def minAvailableDuration(self, slots1, slots2, duration):
          
        slots1.sort()
        slots2.sort()
        
        n1=len(slots1)
        n2=len(slots2)
        
        i=j=0
        
        while i < n1 and j < n2:
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            
            # calculate intersec of two slots
            if min(e1, e2)-max(s1, s2)>=duration:
                return max(s1, s2), max(s1, s2)+duration
              
            # move forward who has smaller ending time  
            if e1 >= e2:
                j += 1
            else:
                i += 1
        return []
