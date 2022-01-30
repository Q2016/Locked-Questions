Question:
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

    
Solution: Dynamic Programming
Optimization: Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two 
left and right end letters are the same. This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, 
and work our way up finding all three letters palindromes, and so on...
steps:
P(i, j) == P(i+1, j-1) && s[i] == s[j];
Base cases :
#One character
P(i, i) = true;
#Two character
P(i, i+1) = s[i] == s[i+1];


        def longestPalindrome(string s):

            n = len(s)
            if (n == 0)
                return ""

            # bool dp[i][j] will be 'True' if the string from index i to j is a palindrome.
            # initialize dp matrix with 0=False

            #Every Single character is palindrome
            for i in range(n):
                dp[i][i] = True
            ans = ""
            ans += s[0]

            for i in range(n - 1,-1):
                for j in range(i + 1,n):
                    if (s[i] == s[j]):
                        #If it is of two character OR if its susbtring is palindrome.
                        if (j - i == 1 or dp[i + 1][j - 1]):
                            #Then it will also be a palindrome substring
                            dp[i][j] = True
                            #Check for Longest Palindrome substring
                            if (len(ans) < j - i + 1):
                                ans = s[i: j - i + 1]
            return ans;



Time Complexity - O(N^2), 
Space Complexity - O(N^2) (caching all substring)
