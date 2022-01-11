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
