Question:
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).
Your goal is to maximize your total score by potentially playing each token in one of two ways:
If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.
Return the largest possible score you can achieve after playing any number of tokens.



Solution: Greedy

If we play a token face up, we might as well play the one with the smallest value. 
Similarly, if we play a token face down, we might as well play the one with the largest value.
We don't need to play anything until absolutely necessary. Let's play tokens face up 
until we can't, then play a token face down and continue.
We must be careful, as it is easy for our implementation to be incorrect if we do not handle 
corner cases correctly. We should always play tokens face up until exhaustion, then play one token face down and continue.
Our loop must be constructed with the right termination condition: we can either play a token face up or face down.
Our final answer could be any of the intermediate answers we got after playing tokens face up (but before playing them face down.)

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans
