Question:
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2. Player 1 and player 2
take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of 
the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The 
player adds the chosen number to their score. The game ends when there are no more elements in the array. Return true if Player 1 can 
win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may 
assume that both players are playing optimally.

Example 1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.	

    
	
	
	
	
	
No link	
	
Solution:
Thus, for the turn of Player 1, we can add its score obtained to the total score and for Player 2's turn, we can substract its score from the 
total score. At the end, we can check if the total score is greater than or equal to zero(equal score of both players), to predict that 
Player 1 will be the winner.

Thus, by making use of a recursive function winner(nums,s,e,turn) which predicts the winner for the nums array as the score array with the elements 
in the range of indices [s,e] currently being considered, given a particular player's turn, indicated by turn=1 being Player 1's turn and turn=−1 
being the Player 2's turn, we can predict the winner of the given problem by making the function call winner(nums,0,n-1,1). Here, n refers to the 
length of nums array.

In every turn, we can either pick up the first(nums[s]) or the last(nums[e]) element of the current subarray. Since both the players are assumed 
to be playing smartly and making the best move at every step, both will tend to maximize their scores. Thus, we can make use of the same function 
winner to determine the maximum score possible for any of the players.

Now, at every step of the recursive process, we determine the maximum score possible for the current player. It will be the maximum one possible 
out of the scores obtained by picking the first or the last element of the current subarray.

To obtain the score possible from the remaining subarray, we can again make use of the same winner function and add the score corresponding to 
the point picked in the current function call. But, we need to take care of whether to add or subtract this score to the total score available. 
If it is Player 1's turn, we add the current number's score to the total score, otherwise, we need to subtract the same.

Thus, at every step, we need update the search space appropriately based on the element chosen and also invert the turn's value to indicate the 
turn change among the players and either add or subtract the current player's score from the total score available to determine the end result.

Further, note that the value returned at every step is given by turn max(turn∗a,turn∗b). This is equivalent to the statement max(a,b) 
for Player 1's turn and min(a,b) for Player 2's turn.

This is done because, looking from Player 1's perspective, for any move made by Player 1, it tends to leave the remaining subarray in a situation 
which minimizes the best score possible for Player 2, even if it plays in the best possible manner. But, when the turn passes to Player 1 again, 
for Player 1 to win, the remaining subarray should be left in a state such that the score obtained from this subarrray is maximum(for Player 1).

This is a general criteria for any arbitrary two player game and is commonly known as the Min-Max algorithm.

public class Solution {
    public boolean PredictTheWinner(int[] nums) {
        return winner(nums, 0, nums.length - 1, 1) >= 0;
    }
    public int winner(int[] nums, int s, int e, int turn) {
        if (s == e)
            return turn * nums[s];
        int a = turn * nums[s] + winner(nums, s + 1, e, -turn);
        int b = turn * nums[e] + winner(nums, s, e - 1, -turn);
        return turn * Math.max(turn * a, turn * b);
    }
}

Complexity Analysis
Time complexity : O(2^n)
Space complexity : O(n) The depth of the recursion tree can go upto n.
	
We can omit the use of turnturn to keep a track of the player for the current turn. To do so, we can make use of a simple observation. If the 
current turn belongs to, say Player 1, we pick up an element, say x, from either end, and give the turn to Player 2. Thus, if we obtain the score 
for the remaining elements(leaving x), this score, now belongs to Player 2. Thus, since Player 2 is competing against Player 1, this score should 
be subtracted from Player 1's current(local) score(x) to obtain the effective score of Player 1 at the current instant.

Similar argument holds true for Player 2's turn as well i.e. we can subtract Player 1's score for the remaining subarray from Player 2's current 
score to obtain its effective score. By making use of this observation, we can omit the use of turnturn from winner to find the required result by 
making the slight change discussed above in the winner's implementation.

While returning the result from winner for the current function call, we return the larger of the effective scores possible by choosing either 
the first or the last element from the currently available subarray. Rest of the process remains the same as the last approach.

Now, in order to remove the duplicate function calls, we can make use of a 2-D memoization array, memomemo, such that we can store the result 
obtained for the function call winner for a subarray with starting and ending indices being s and e] at memo[s][e]. This helps to prune the 
search space to a great extent.	

public class Solution {
    public boolean PredictTheWinner(int[] nums) {
        Integer[][] memo = new Integer[nums.length][nums.length];
        return winner(nums, 0, nums.length - 1, memo) >= 0;
    }
    public int winner(int[] nums, int s, int e, Integer[][] memo) {
        if (s == e)
            return nums[s];
        if (memo[s][e] != null)
            return memo[s][e];
        int a = nums[s] - winner(nums, s + 1, e, memo);
        int b = nums[e] - winner(nums, s, e - 1, memo);
        memo[s][e] = Math.max(a, b);
        return memo[s][e];
    }
} 

Complexity Analysis
Time complexity : O(n^2)
Space complexity : O(n^2)    
