Question: (Hard)
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock 
patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys. Rules for a valid pattern:
Each pattern must connect at least m keys and at most n keys. All the keys must be distinct. If the line connecting two 
consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. 
No jumps through non selected key is allowed. The order of keys used matters.


Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Based on the rules above:
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.
Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.
Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.


Solution:
https://medium.com/@rebeccahezhang/leetcode-351-android-unlock-patterns-d9bae4a8a958  

We sum all the valid patterns when using m keys, m+1 keys, … n keys together to get the result.
In each case, we use DFS to count the number of valid paths from the current number (1–9) to 
the remaining numbers. To optimize, calling DFS less than 9 times, we can use the symmetry of 
the 3 by 3 matrix. If we start from 1 or 3 or 7 or 9, the valid paths number should be the same. 
If we start from 2 or 4 or 6 or 8, the valid paths number are also the same. Start from 5 is the third case. So the total is :
return value of DFS (start from 1) * 4 + return value of DFS (start from 2) * 4 + return value of DFS (start from 5)
One of the invalid case can be: I want to create a pattern using 1 and 3. First you touch 1, moving your finger to the right to 
reach 3 — oh no, there is 2 in the middle that we don’t want it in my password! Here are all the invalid patterns:
start key | end key | unselected number on the path
        1 | 3       | 2
        3 | 1       | 2
        1 | 7       | 4
        7 | 1       | 4
        3 | 9       | 6
        9 | 3       | 6
        7 | 9       | 8
        9 | 7       | 8
        1 | 9       | 5
        9 | 1       | 5
        2 | 8       | 5
        8 | 2       | 5
        3 | 7       | 5
        7 | 3       | 5
        4 | 6       | 5
        6 | 4       | 5
We need to create a matrix to keep a record of unselected numbers on the path between two keys.
Now in DFS, we keep trying to find the next valid key. What is a valid candidate? We need 
to make sure if the next key hasn’t been visited, and either it’s adjacent to the current key, 
or it’s the key in between (recorded as the unselected number on the path) but has been visited.

class Solution {
    public int numberOfPatterns(int m, int n) {
        // Keep a recod of invalid numbers on the path between 
        // two selected keys 
        int skip[][] = new int[10][10];
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
        boolean visited[] = new boolean[10];
        int res = 0;
        for (int i = m; i <= n; i++) {
            // Use the symetry to reduce DFS call
            res += DFS(visited, skip, 1, i - 1) * 4;
            res += DFS(visited, skip, 2, i - 1) * 4;
            res += DFS(visited, skip, 5, i - 1);
        }
        return res;
    }
  
     public int DFS(boolean[] visited, int[][] skip, int cur, int remain) {
        // Base case: out of bound
        if (remain < 0) return 0;
        // Base case: no remaining numbers
        if (remain == 0) return 1;
        // Mark number as visited
        visited[cur] = true;
        int res = 0;
        // ?
        for (int i = 1; i <= 9; i++) {
            // Next key must be unvisited
            // Current key and next key are adjacent or skip number is already visited
            if (!visited[i] && (skip[cur][i] == 0 || visited[skip[cur][i]])) {
                res += DFS(visited, skip, i, remain-1);
            }
        }
        // Mark as unvisited for the rest of recursion calls after return from the first one  
        visited[cur] = false;
        return res;
    }
}   







