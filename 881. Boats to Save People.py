Question:
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can 
carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)    

    
    
    
    
    
    
    
    
Solution: Greedy (Two Pointer)

If the heaviest person can share a boat with the lightest person, then do so. Otherwise, 
the heaviest person can't pair with anyone, so they get their own boat.
The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.
Let people[i] to the currently lightest person, and people[j] to the heaviest.
Then, as described above, if the heaviest person can share a boat with the lightest person 
(if people[j] + people[i] <= limit) then do so; otherwise, the heaviest person sits in their own boat.


class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort() # nlog n
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

    
    
Complexity Analysis

Time Complexity: O(NlogN), where N is the length of people.

Space Complexity: O(logN).
Some extra space is used when we sort people in place. The space complexity of the sorting algorithm depends on which sorting algorithm is used; 
the default algorithm varies from one language to another.
In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with worst-case space complexity of O(logn).
In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logn).
In python, the sort method sorts a list using the Timsort algorithm, which is a combination of Merge Sort and Insertion Sort and uses O(n) additional 
space.   

From the comments under leetcode 'solution' tab:

The "add as many people possible to a boat" part is itself a DP problem, similar to the stone smashing problem 
(https://leetcode.com/problems/last-stone-weight-ii/) or partitioning a list into two equal subsets. In the stone smashing problem, 
the DP problem is dp[i] = the closest value we can approximate to i using numbers in the list, with the ultimate goal of solving for 
dp[sum(list) / 2]. This takes O(NW) to solve where W is sum(list) / 2 and N is the number of elements in the list. In our case, we'd set W to 
limit, so O(N*limit). Then we have to repeat this for every single boat we fill, and the number of boats is bounded by N. So O(limit * N^2). 
I think this is how you would do the boat filling algorithm for each individual boat



using namespace std;

class Solution {
public:
    int solution(vector<int>& weights, int limit) {
        int n = weights.size();

        vector<int> dp(limit+1, 0);
        
        // dp[j] is the closest approximation we can get to a sum of j
        // using a subset (or all) of the weights we have seen so far. 
        
        for(int weight: weights)
            for(int j = limit; j >=weight; j--) {
                dp[j] = max(dp[j] , weight + dp[j - weight]);
            }

        return dp.back();
    }
};
@th015 The koko eating bananas approach is not quite applicable here. The banana-eating rate is analogous to the boat capacity, and in 
the koko problem, it's ok for us to waste time (when the amount of bananas remaining in the pile is < your eating rate). However, in this 
boat problem, we don't want to waste "time" (analogous to space in each boat). Checking if our binary search guess is correct would entail a 
careful DP solver as described above. However, if you're going to do the above DP problem, you would end up getting the correct number of 
boats without the binary search. You would just repeat the O(N * limit) algorithm as many times as you needed until you had no one left.


