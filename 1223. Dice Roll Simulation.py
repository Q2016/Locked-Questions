
Solution:
https://leetcode.com/problems/dice-roll-simulation/discuss/404840/Short-Python-DP-with-detailed-image-explanation  


Here I illustrate the idea with the example: Input: n = 3, rollMax = [1,1,1,2,2,3]. Output: 181.

Also the definition of DP array:

for j = 0, 1, ..., faces - 1
dp[i][j] means how many combinations it could be that at i-th rolling and the last face is j
for j = faces
dp[i][j] means how many combinations it could be that at i-th rolling in total
Basically on every [i][j], we are trying to climb up in the column [j], and how many steps we could climb up is based on rollMax[j].

image

Another example: let's say we roll dice i = 5 times, and the last face is j = 5, then we have this sequence xxxx5 where x could ranges from 0 to 5 arbitrarily if we are not restricted. Then let's calculate how many combinations we could form xxxx5 with constraint rollMax[j] = 3. They could be categorized as follow:

step1: xxxy5, where x in [0, 5] and y in [0, 4], this means from the end 5, we have consecutive one 5
step2: xxy55, this means from the end 5, we have consecutive two 5
step3: xy555, this means from the end 5, we have consecutive three 5
We could not climb the column upper because we are restricted to only be able to climb up rollMax[j] = 3 steps.
Then the question is how to calculate the combinations of ...xy. Actually if you take a deeper look, what ...xy means is essentially: give me all the combinations as long as the last face is not 5. We don't care what x should be here because it is not restricted and could choose any value (it could be even same as y, or same as 5). As long as y is not equal to 5, we are good to go. And that is the definition dp[i][j]!

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        # [n + 1][faces + 1] dimensional dp array
        dp = [[0 for i in range(faces + 1)] for j in range(n + 1)]
        
        # initialization
        # roll 0 times, the total combination is 1
        dp[0][faces] = 1
        # roll 1 times, the combinations that end at face j is 1
        for j in range(faces):
            dp[1][j] = 1
        # roll 1 times, the total combination is faces = 6
        dp[1][faces] = faces
        
        # then roll dices from 2 times, until n times
        for i in range(2, n + 1):
            # iterate through each column (face)
            for j in range(faces):
                # at each [i, j], trying to go up (decrease i) and collect all the sum of previous state
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][faces] - dp[i - k][j]
            # update total sum of this row
            dp[i][faces] = sum(dp[i])
        
        return dp[n][faces] % 1000000007
