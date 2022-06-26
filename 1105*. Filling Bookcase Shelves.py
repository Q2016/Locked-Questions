Question:
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness 
and height of the ith book. You are also given an integer shelfWidth.
We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.	

photo: https://leetcode.com/problems/filling-bookcase-shelves/

		
		
we need to see the video of this problem, dont understand the question		
		
		
		
		
		
		
	
	
Solution: 2D knapsack problem
	
You can read about knapSack in Q2016/Cheat-sheet	
	
public int minHeightShelves(int[][] books, int shelf_width) {
		int n = books.length;
		// vidx, width, height
		int[][] dp = new int[n + 1][shelf_width];

		return minHeightShelves(books, 1, shelf_width - books[0][0], books[0][1], shelf_width, dp);
	}

	// using TopDown
	public int minHeightShelves(int[][] books, int vidx, int currWidth, int currHt, int shelf_width, int[][] dp) {
		if (vidx == books.length) {
			return dp[vidx][currWidth] = currHt;
		}
		if (dp[vidx][currWidth] != 0) {
			return dp[vidx][currWidth];
		}
		int currBookWidth = books[vidx][0];
		int currBookHeight = books[vidx][1];

		int sameShelf = (int) 1e8;
		if (currWidth - currBookWidth >= 0) {
			sameShelf = minHeightShelves(books, vidx + 1, currWidth - currBookWidth, Math.max(currHt, currBookHeight),
					shelf_width, dp);
		}
		int nextShelf = (int) 1e8;
		if (currBookWidth <= shelf_width) {
			int temp = currHt;
			nextShelf = minHeightShelves(books, vidx + 1, shelf_width - currBookWidth, currBookHeight, shelf_width, dp)
					+ temp;
		}
		return dp[vidx][currWidth] = Math.min(sameShelf, nextShelf);
	}
  
  
  
