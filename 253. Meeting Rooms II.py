Question:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...], find the minimum number 
of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]], Output: 2
  
  
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
