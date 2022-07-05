Question:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...], find the minimum number 
of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]], Output: 2
  
  
  
  
  
  
  
  
  
  
  
  
Basically number of bounds that have interactions  
  
Solution:  Two pointers
  
https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/meeting-rooms-ii.py


    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort() # O(nlogn)

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1
        return min_rooms  
      
      
# Time:  O(nlogn)
# Space: O(n)      



Meeting Rooms I:

Question:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), determine if a person could attend all meetings.
(person cant jump from one meeting to another unless it's finished)

Example 1
Input: [[0,30],[5,10],[15,20]]
Output: false


Solution:
Sort the list by start time and iterate the sorted list. If the current start time is less than previous end time, then there is conflict 
and you can not attend all meeting.

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
            new_intervals = sorted(intervals, key=lambda x: x[0])
            for i in range(1,len(new_intervals)):
                if new_intervals[i-1][1] > new_intervals[i][0]:return False
            return True

Time complexity : O(nlogn + n) since sort the list will take O(nlogn) and iteration will take O(n) 
where n is the size of input. Sum up the time complexity is O(nlogn)
