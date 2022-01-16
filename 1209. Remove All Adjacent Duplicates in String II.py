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
