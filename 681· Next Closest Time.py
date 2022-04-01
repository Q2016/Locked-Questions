Question:
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on 
how many times a digit can be reused. You may assume the given input string is always valid. For example, "01:34", "12:09" are valid. 
"1:34", "12:9" are invalid.

Example
Example 1:
Input: "19:34"
Output: "19:39"
Explanation:
The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:
Input: "23:59"
Output: "22:22"
Explanation: It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
    



solution:


def nextClosestTime(time):
    # write your code here
    
    #digits=[s for s in time if s!=':']
    #cur_value=int(digits[0]+digits[1])*60+int(digits[2]+digits[3])
    
    def calc_value(time):
        value=int(digits[0]+digits[1])*60+int(digits[2]+digits[3])
        return value 
    
    digits=[s for s in time if s!=':']
    
    min_time=0
    dic={}
    for i,n in enumerate(digits[::-1]):
        for j in [k for k in digits if k>n]:
            copy=digits
            copy[i]=j
            min_time=min(min_time,calc_value(copy))
            dic[str(i)+str(j)]=min_time
    
    # max is 24*60
    # replace the min with all for cases that didnt pass above
    
    return digits



time="19:34"
print(nextClosestTime(time))


######################################################################
https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/next-closest-time.py
# Line 53 means set(result) is a subset of set(time) according to:https://stackoverflow.com/questions/49677114/comparing-two-sets-in-python
class Solution(object):
    def nextClosestTime(self, time):

        h, m = time.split(":")
        curr = int(h) * 60 + int(m)
        result = None
        for i in xrange(curr+1, curr+1441):
            t = i % 1440
            h, m = t // 60, t % 60
            result = "%02d:%02d" % (h, m)
            if set(result) <= set(time):
                break
        return result
