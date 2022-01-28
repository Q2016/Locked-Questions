Question:
Given a string that contains + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person
can no longer make a move and therefore the other person will be the winner. Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++", return true. The starting player can guarantee 
a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.


Solution: Bactracking

 
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
    

   
