Question:
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent 
and equal letters from s and removing them, causing the left and the right side of the deleted 
substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. 

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"     


Solution: DP or Stack

class Solution {
public:
     string removeDuplicates(string s, int k) {
      for (auto i = 1, cnt = 1; i < s.size(); ++i) {
        if (s[i] != s[i - 1]) cnt = 1;
        else if (++cnt == k)
          return removeDuplicates(s.substr(0, i - k + 1) + s.substr(i + 1), k);
      }
      return s;
    }
};

/*
Approach 1: Brute-force
Just keep removing duplicates until there is no more. When we find a duplicate, we call the same function recursively with that duplicate removed.

string removeDuplicates(string s, int k) {
  for (auto i = 1, cnt = 1; i < s.size(); ++i) {
    if (s[i] != s[i - 1]) cnt = 1;
    else if (++cnt == k)
      return removeDuplicates(s.substr(0, i - k + 1) + s.substr(i + 1), k);
  }
  return s;
}


// stack

class Solution {
public:
    string removeDuplicates(string S, int K) {
        int i, j;
        stack<int> st;
        st.push(0);
        for (i = 1, j = 1; j < S.size(); i++, j++) {
            S[i] = S[j];
            if (i == 0 || S[i] != S[i-1]) st.push(i);
            else if (i - st.top() + 1 == K) {
                i = st.top() - 1;
                st.pop();
            }
        }
        return S.substr(0, i);
    }
};
*/
