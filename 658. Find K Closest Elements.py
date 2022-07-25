Question:
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also 
be sorted in ascending order. An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or |a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]	


	
	
	
	
	
	
One intuitive way of solving this is to use BST to find the number and then use left/right pointers to add values.
But the stanadard solution is shorter but harder to understand. Complexity is same both methods.

The idea of the latter solution is that, we dont search for the target value but the target window.

Solution: BST
	https://www.youtube.com/watch?v=o-YDQzHoaKM
		
class Solution:
    def findClosestElements(self, arr, k, x):
	l, r=0,len(arr)-k
	
	while l<r:
	    m=(l+r)//2
	    if x-arr[m]>arr[m+k]-x:# uses examples to find out
	       l=m+1
	    else:
		r=m
	    
	return arr[l:l+k]
	
		
		
		
		
		
		
		
		
We need to return k elements that are closest to x. The input array is sorted in ascending order. So, we will try to find the 
starting point of these k elements i.e. the first element in this list of k elements which will make it easier to return the k elements. 
Let's call this first element of the output list start. Obviously, start will lie between indices 0 and length - k where length is the 
length of the array. So, it makes sense to perform binary search on this section only. Therfore, we initialize left=0 and right = len(arr) - k
Because we have to return k elements, it also makes sense to consider a window of k elements for comparison.
Consider the following boundaries for the element x: left ......... mid ......... mid + k ......... right
x <= arr[mid]
arr[mid + k] <= x
arr[mid] < x < arr[mid + k]

Case 1 : x <= arr[mid]
If x is less than arr[mid] then it's clear that arr[mid + k] cannot be a part of our output k elements. This is because there are k + 1 elements 
between arr[mid] and arr[mid + k] inclusive. So, the start will either be mid or towards the left of it.
Case 2 : arr[mid + k] <= x
Similar to previous case, arr[mid] cannot be a part of our output k elements because of the k + 1 elements we have in between. Therefore, start 
will lie towards the right of mid.
Case 3 : arr[mid] < x < arr[mid + k]
This is more like a combination of the above two cases.
A. If x is closer to arr[mid] then just like our case 1, arr[mid + k] cannot be a part of our output k elements. Therefore, our start will either 
be mid or towards the left of it.
B. If x is closer to arr[mid + k], then just like case 2, arr[mid] cannot be a part of our output k elements, which means that our start will lie 
towards the right of mid.

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)//2
			
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
        
                    
