Question:
Given a string that contains + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person
can no longer make a move and therefore the other person will be the winner. Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++", return true. The starting player can guarantee 
a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.

Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".













Solution: Bactracking or Recursive

 
    def canWin(s):
        if len(s)== 0) :
            return false
        arr = list(s)
        return canWinHelper(arr)
    
    def canWinHelper(arr) :
         
        for i in range(0, len(arr)):
            if (arr[i] == '+' and arr[i + 1] == '+') :
                arr[i] = '-'
                arr[i + 1] = '-' 
                win = Not canWinHelper(arr);
                # Backtracking
                arr[i] = '+'
                arr[i + 1] = '+'
                if win:
                    return true
        return false
    
I dont know how to derive this?
T(N) = T(N-2) + T(N-3) + [T(2) + T(N-4)] + [T(3) + T(N-5)] + ... [T(N-5) + T(3)] + [T(N-4) + T(2)] + T(N-3) + T(N-2)
     = 2 * sum(T[i])  (i = 3..N-2)
the runtime complexity will be expotential.   



or

    def canWin(s) :
       n=len(s)
       if s==None or n<2:
          return False
    
       for i in range(n):
          if (s[i]=='+' and s[i+1]=='+'):
              nextState=s[:i]+'--'+s[i+2:]
              if !canWin(nextState):
                 return True
