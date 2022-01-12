Solution: (Divide And Conquer)


//in the first pass I record counts of every character in a hashmap
//in the second pass I locate the first character that appear less than k times in the //string. this character is definitely not included in the result, and that separates the //string into two parts.
//keep doing this recursively and the maximum of the left/right part is the answer.


class Solution {
public:

    int longestSubstring(string s, int k) {
        if(s.size() == 0 || k > s.size())   return 0;
        if(k == 0)  return s.size();
        
        unordered_map<char,int> Map;
        for(int i = 0; i < s.size(); i++){
            Map[s[i]]++;
        }
        
        int idx =0;
        while(idx <s.size() && Map[s[idx]] >= k)    idx++;
        if(idx == s.size()) return s.size();
        
        int left = longestSubstring(s.substr(0 , idx) , k);
        int right = longestSubstring(s.substr(idx+1) , k);
        
        return max(left, right);
        
    }
};
