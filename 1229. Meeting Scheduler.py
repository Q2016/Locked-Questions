Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []


Intuition:I am here to provide a non-pq approach. Intervals of the first two terms of the start time sequence, 
  after traversing the pointers are double Intervals two people, while looking for the possible start and end 
  of each interval in which, if satisfied start + duration <= end of the recording start and the current end. 
  If there is no such case it returns an empty list.

Time O (nlogn) - sort

Space O (1)
  
  
  
      def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
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
