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
       
        def cmpf(v1,v2):
            return v1[0] - v2[0]
          
        slots1.sort(cmp=cmpf)
        slots2.sort(cmp=cmpf)
        inx1 = inx2 = 0
        while inx1 < len(slots1) and inx2 < len(slots2):
            item1 = slots1[inx1]
            item2 = slots2[inx2]
            if item1[0] > item2[1]:
                inx2 += 1
            elif item1[1] < item2[0]:
                inx1 += 1
            else:
                ms = max(item1[0],item2[0])
                me = min(item1[1],item2[1])
                if me - ms >= duration:
                    return [ms,ms+duration]
                if item1[1] < item2[1]:
                    inx1 += 1
                else:
                    inx2 += 1
        return []
