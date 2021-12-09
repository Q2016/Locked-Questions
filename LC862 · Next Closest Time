##############################################################
My solution


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
        """
        :type time: str
        :rtype: str
        """
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
