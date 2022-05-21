Question:
You have an initial power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token.
Your goal is to maximize your total score by potentially playing each token in one of two ways:
If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.
Return the largest possible score you can achieve after playing any number of tokens.













Solution: Greedy (The conditions are important, the idea is easy)

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

    
Complexity Analysis

Time Complexity: O(NlogN), where N is the length of tokens.

Space complexity : O(N) or O(logN) 
The space complexity of the sorting algorithm depends on the implementation of each program language.
    For instance, the sorted() function in Python is implemented with the Timsort algorithm whose space complexity is O(N).
    In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose space complexity is O(logN).
 


Another solution: Two pointers
    
Looks simpler to use just one loop and play token face down only when you have at least one more token left:
Java:
        Arrays.sort(tokens);
        if (tokens.length == 0 || power < tokens[0]) return 0;
        int left = 0, right = tokens.length - 1, points = 0;
        while (left <= right) {
            if (power >= tokens[left]) {
                points++;
                power -= tokens[left];
                left++;
            } else {
                if (right - left > 1) {
                    power += tokens[right];
                    right--;
                    points--;
                } else break;
            }
        }
        return points;    
