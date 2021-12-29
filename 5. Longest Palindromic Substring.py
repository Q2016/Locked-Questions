/*Approach 3: Dynamic Programming
To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.
This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...\


How Can we optimise our code?

Got it in above solution, we do unnecessary recompution while validating palindomes.
For example : if we know string "aba" is palindrome then "cabac" must be palindrome as left and right are equal.

Solution 2: Using DP

P(i, j) == P(i+1, j-1) && s[i] == s[j];

Base cases :

//One character
P(i, i) = true;

//Two character
P(i, i+1) = s[i] == s[i+1];

Time Complexity - O(N^2), Space Complexity - O(N^2) (caching all substring)
*/

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int n = s.size();
        if (n == 0)
            return "";

        // dp[i][j] will be 'true' if the string from index i to j is a palindrome.
        bool dp[n][n];

        //Initialize with false

        memset(dp, 0, sizeof(dp));

        //Every Single character is palindrome
        for (int i = 0; i < n; i++)
            dp[i][i] = true;

        string ans = "";
        ans += s[0];

        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (s[i] == s[j])
                {
                    //If it is of two character OR if its susbtring is palindrome.
                    if (j - i == 1 || dp[i + 1][j - 1])
                    {
                        //Then it will also a palindrome substring
                        dp[i][j] = true;

                        //Check for Longest Palindrome substring
                        if (ans.size() < j - i + 1)
                            ans = s.substr(i, j - i + 1);
                    }
                }
            }
        }
        return ans;
    }
};
