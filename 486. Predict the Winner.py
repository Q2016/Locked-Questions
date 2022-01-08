class Solution(object):
    
    def PredictTheWinner(self, nums):
        m=0 #me
        n=0 #him
        score(nums)
        return m>n 
    
    
    def score(self, nums,):
        if len(nums) <= 2:
			# If there are only 2 numbers, obviously we'll choose the greatest number
            return max(nums)
        
        # my_score function will return the score of the opponent
        choose_first = self.score(nums[1:], summ-nums[0])
        choose_last = self.score(nums[:-1], summ-nums[-1])
        
        return max(summ - choose_first, summ - choose_last) 
    
    
    
    
    
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
