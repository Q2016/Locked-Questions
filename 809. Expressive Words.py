My solution:

def expressiveWords(s, words):
    
    
    l2=len(s)
    n=0
    for word in words:
        
        
        start1=0
        start2=0
        end2=0
        flag=True
        
        l1=len(word)
        
        while start1<l1 and end2 <l2:
            # assuming the first char is equal
            if start2+1<l2 and start1+1<l1:
                if s[start2]==word[start1] and s[start2+1]==word[start1+1]:
                    start1+=1
                    start2+=1
                    end2=start2
                else:
                    print(word)
                    print(start1,end2)
                    while s[end2+1] != word[start1+1]:
                        end2+=1
                    cnt=end2-start2
                    if 0<cnt<2:
                        flag=False
                        break   
                    start2=end2
                
                
        if flag==True:
            n+=1
            
    return n

s="heeellooo"
words=["hello", "hi", "helo"]
print(expressiveWords(s, words))










https://leetcode.com/problems/expressive-words/discuss/121706/Java-Solution-using-Two-Pointers-with-Detailed-Explanation

We have two pointers, use i to scan S, and use j to scan each word in words.
Firstly, for S and word, we can calculate the length of the susbtrings which contains the repeated letters of the letter currently pointed by the two pointers, and get len1 and len2.

The two letters currently pointed by the two pointers must be equal, otherwise the word is not stretchy, we return false. Then, if we find that len1 is smaller than 3, it means the letter cannot be extended, so len1 must equals to len2, otherwise this word is not stretchy. In the other case, if len1 equals to or larger than 3, we must have len1 equals to or larger than len2, otherwise there are not enough letters in S to match the letters in word.

Finally, if the word is stretchy, we need to guarantee that both of the two pointers has scanned the whole string.

class Solution {
    public int expressiveWords(String S, String[] words) {
        if (S == null || words == null) {
            return 0;
        }
        int count = 0;
        for (String word : words) {
            if (stretchy(S, word)) {
                count++;
            }
        }
        return count;
    }
    
    public boolean stretchy(String S, String word) {
        if (word == null) {
            return false;
        }
        int i = 0;
        int j = 0;
        while (i < S.length() && j < word.length()) {
            if (S.charAt(i) == word.charAt(j)) {
                int len1 = getRepeatedLength(S, i);
                int len2 = getRepeatedLength(word, j);
                if (len1 < 3 && len1 != len2 || len1 >= 3 && len1 < len2) {
                    return false;
                }
                i += len1;
                j += len2;
            } else {
                return false;
            }
        }
        return i == S.length() && j == word.length();
    }
    
    public int getRepeatedLength(String str, int i) {
        int j = i;
        while (j < str.length() && str.charAt(j) == str.charAt(i)) {
            j++;
        }
        return j - i;
    }
}
