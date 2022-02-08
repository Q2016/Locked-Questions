Question:
Imagine you have a special keyboard with the following keys:
Key 1: (A): Prints one 'A' on screen.
Key 2: (Ctrl-A): Select the whole screen.
Key 3: (Ctrl-C): Copy selection to buffer.
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 7, Output: 9, Explanation: We can at most get 9 A's on screen by pressing following key sequence: A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V


Solution:
This problem has many solutions:  # http://bookshadow.com/weblog/2017/07/30/leetcode-4-keys-keyboard/

    def maxA(self, N):

        dp = collections.defaultdict(lambda : collections.defaultdict(int))
        dp[0][0] = 0 #step, buffer
        for z in range(N):
            for y in dp[z]:
                #Key 1: (A):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)
                #Key 4: (Ctrl-V):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)
                #Key 2: (Ctrl-A): + Key 3: (Ctrl-C):
                dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])
        return max(dp[N].values())
