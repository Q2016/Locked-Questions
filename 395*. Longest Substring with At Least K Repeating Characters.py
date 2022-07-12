Question:
Given a string s and an integer k, return the length of the longest substring of s such that the 
frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

    
    
    
    
    
    
    
    
Obvious solution is sliding window. But it's a bit hard   
    
Solution: 
    https://www.youtube.com/watch?v=eNCYapoYsBw
    
class Solution:
    def longestSubstring(self, s, k):
        freq= Counter(s)
        max_nums=len(freq)
        n=len(s)
        ans=0
        
        
        for num in range(1, max_nums+1):
            counter=defaultdict(int)
            
            left=0
            
            for right in range(n):
                counter[s[right]] +=1
                
                # maintain the sliding window
                while len(counter)> num:
                    counter[s[left]] -=1
                    if counter[s[left]]==0:
                        del counter[s[left]]
                        
                    left += 1
                    
                # now with a valid sliding window, we check the frequency
                if all(count >=k for key, count in counter.items()):
                    ans =max(ans, right-left+1)
                    
        return ans

    
Time O(n)    
    
    
    
    
Divide And Conquer:
    
def partition(left, right):
    counter=defaultdict(int)
    
    for i in range(left, right+1):
        counter[s[i]] +=1
        
    for mid in range(left, right+1):
        if counter[s[mid]]<k:
            return max(partition(left, mid-1), partition(mid+1,right))
    
    return right-left+1

n=len(s)
return partition(0, n-1)

Worst time O(n^2)
Best time O(nlogn)



