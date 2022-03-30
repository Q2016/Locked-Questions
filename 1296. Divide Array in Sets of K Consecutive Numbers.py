Question:
Given an array of integers nums and a positive integer k, check whether it is possible to 
divide this array into sets of k consecutive numbers. Return true if it is possible. Otherwise, return false.

Example 1:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].    
    
    
    
    
    
    
    
Solution: Greedy (look at the comments at the python question)

We can use a greedy approach and start with the smallest number and see if the numbers from that number + k exist and then keep 
removing them from the numbers we have, if there is a case where it's not possible then we return false.



class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) 
    {
        if(nums.size()%k!=0)
            return false;
        map<int,int> count;
        map<int,int>::iterator it;
        int freq;
        for(int &i:nums)  #Store the count of all numbers sorted.
            count[i]++;
        for(it=count.begin();it!=count.end();it++)	#Start with the smallest number.
            if(it->second)		#If the count of smallest integer is non 0 check if next k numbers exist and have atleast same frequency.
            {
                freq=it->second;
                for(int i=0;i<k;i++)	#Checks for the next k-1 numbers.
                    #We are unable to find ith consecutive number to the smallest(starting number) with atleast same frequency.
                    if(count[it->first+i]<freq) 
                        return false;
                    else
                        count[it->first+i]-=freq;       #Reduce the count of the numbers used.
            }
        return true;
    }
};

Complexity
Space: O(n). Since we store the count of all the numbers.
Time: O(nlogn). Since we use map which is sorted and each lookup is O(logn).    
    

from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for n in sorted(count):
            if count[n] > 0:
                need = count[n]
                for i in range(n,n+k): # because we want k consecutive numbers
                    if count[i] < need: # what we need (at least), otherwise cant have consequtives in one group
                        return False
                    count[i] -= need
        return True
        

