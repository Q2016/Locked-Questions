Question:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).    



Solution:
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic={}
        for i,p in enumerate(points):
            dic[i]=p[0]**2+p[1]**2
        
        
        dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
        print(dic)
        pairs = iter((dic.items()))
        
        arr=[]   
        for i,d in enumerate(dic):
            if i<k:
                #print(points[next(pairs)[0]])
                arr.append(points[next(pairs)[0]])
        return arr
        
        
        
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
