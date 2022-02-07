Question:
You are given an m x n char matrix board representing the game board where:
'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and 'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').
Return the board after revealing this position according to the following rules:
If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent 
unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.    

Solution: DFS

    def updateBoard(board, click) :
        if(board[click[0]][click[1]] == 'M'):
            board[click[0]][click[1]] = 'X';
            return board;
        reveal(board,click[0],click[1]);
        return board;
     
    def inboard(board, x, y):
        return ( x>=0 && x<board.size() && y>=0 && y<board[0].size() );
       
    def reveal(board, x, y):
        if(!inboard(board,x,y)) return;
        if(board[x][y] == 'E'):
            #search 8 adjacent squares
            count = 0;
            # we can replace it with directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
            if(inboard(board,x-1,y-1) && board[x-1][y-1] == 'M') count++;
            if(inboard(board,x-1,y  ) && board[x-1][y  ] == 'M') count++;
            if(inboard(board,x-1,y+1) && board[x-1][y+1] == 'M') count++;
            if(inboard(board,x  ,y-1) && board[x  ][y-1] == 'M') count++;
            if(inboard(board,x  ,y+1) && board[x  ][y+1] == 'M') count++;
            if(inboard(board,x+1,y-1) && board[x+1][y-1] == 'M') count++;
            if(inboard(board,x+1,y  ) && board[x+1][y  ] == 'M') count++;
            if(inboard(board,x+1,y+1) && board[x+1][y+1] == 'M') count++;

            if(count>0):
                board[x][y] = '0'+count;
            else:
                board[x][y] = 'B';
                reveal(board,x-1,y-1);
                reveal(board,x-1,y  );
                reveal(board,x-1,y+1);
                reveal(board,x  ,y-1);
                reveal(board,x  ,y+1);
                reveal(board,x+1,y-1);
                reveal(board,x+1,y  );
                reveal(board,x+1,y+1);

