Question:
Given a positive integer n and you can do operations as follow: If n is even, replace n with n/2. If n is odd, 
you can replace n with either n + 1 or n - 1. What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:8, Output: 3, Explanation: 8 -> 4 -> 2 -> 1

                  
                  
                  
                  
                  
                  
              
              
              
          
          
          
          
              
Time complexity of DP version was in the interview              
      
Solution: BFS   
https://www.youtube.com/watch?v=5ksn2Myjlig
  
def integerReplacement(self, n):
    queue=deque([n])
    seen=set()
    seen.add(n)
    ans=0
    while queue:
        for _ in range(len(queue)):
            cur=queue.poplef()

            if cur==1:
              return and

            # odd number
            if cur %2:
              if cur+1 not in seen:
                queue.append(cur+1)
                seen.add(cur+1)

              if cur-1 not in seen:
                queue.append(cur-1)
                seen.add(cur-1)

            else:
              if cur//2 not in seen:
                queue.append(cur//2)
                seen.add(cur//2)

        ans+=1
   return ans
  
Time O(log n)  
  
  
  
Solution 2: DP  
  
The point about the DP is that, we can only solve it top-down. Time complexity of DP is also O(log n) because of the n//2 operations.
  
  
(We do direct approach similar to 1342.)    

Denote f(n) the minimum number of jumps from n to 1. By definition, we have the recurrence 
f(1) = 0, f(2n) = 1 + f(n), f(2n + 1) = min(f(2n) + 1, f(2n + 2) + 1). First notice that this sequence is well defined 
because f(2n + 2) = f(n + 1) + 1, so f(2n + 1) = min(f(2n) + 1, f(n + 1) + 2). Every element is defined by some element before it.

    def integerReplacement(self, n):
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n//2, memo)
            return memo[n]
