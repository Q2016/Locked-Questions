Approach 1: Backtracking

Intuition:
https://leetcode.com/problems/palindrome-partitioning/solution/  

The idea is to generate all possible substrings of a given string and expand each possibility if is a potential candidate. The first thing that comes to our mind is Depth First Search. In Depth First Search, we recursively expand potential candidate until the defined goal is achieved. After that, we backtrack to explore the next potential candidate.

Backtracking incrementally build the candidates for the solution and discard the candidates (backtrack) if it doesn't satisfy the condition.

The backtracking algorithms consists of the following steps:

Choose: Choose the potential candidate. Here, our potential candidates are all substrings that could be generated from the given string.

Constraint: Define a constraint that must be satisfied by the chosen candidate. In this case, the constraint is that the string must be a palindrome.

Goal: We must define the goal that determines if have found the required solution and we must backtrack. Here, our goal is achieved if we have reached the end of the string.

Algorithm

In the backtracking algorithm, we recursively traverse over the string in depth-first search fashion. For each recursive call, the beginning index of the string is given as \text{start}start.

Iteratively generate all possible substrings beginning at \text{start}start index. The \text{end}end index increments from \text{start}start till the end of the string.

For each of the substring generated, check if it is a palindrome.

If the substring is a palindrome, the substring is a potential candidate. Add substring to the \text{currentList}currentList and perform a depth-first search on the remaining substring. If current substring ends at index \text{end}end, \text{end}+1end+1 becomes the \text{start}start index for the next recursive call.

Backtrack if \text{start}start index is greater than or equal to the string length and add the \text{currentList}currentList to the result.
    
    
    
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> currentList;
        dfs(result, s, 0, currentList);
        return result;
    }

    void dfs(vector<vector<string>> &result, string &s, int start, vector<string> &currentList) {
        if (start >= s.length()) result.push_back(currentList);
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                // add current substring in the currentList
                currentList.push_back(s.substr(start, end - start + 1));
                dfs(result, s, end + 1, currentList);
                // backtrack and remove the current substring from currentList
                currentList.pop_back();
            }
        }
    }

    bool isPalindrome(string &s, int low, int high) {
        while (low < high) {
            if (s[low++] != s[high--]) return false;
        }
        return true;
    }
};    
