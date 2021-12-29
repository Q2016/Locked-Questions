Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.

things to consider: 1 does each group allow duplicates, such as ["a", "a"]. 2 how to calculate unique hash key.
  


  
Explanation:
  
This problem is very easy.
The basic idea is to shift all words back into the form starting with 'a'. (all digits must shift the same distance). If the two words share the same shifted word, it means they actually come from the same shift group. 

Thus I have developed a shiftStr function for this purpose.
private String shiftStr(String str) {
    StringBuffer buffer = new StringBuffer();
    char[] char_array = str.toCharArray();
    int dist = str.charAt(0) - 'a';
    for (char c : char_array) 
        buffer.append((c - 'a' - dist + 26) % 26 + 'a');
    return buffer.toString();
}

Step 1: get the distance each word must shift (leftward, it actually does not matter). Use the first character of a Word, and compute the distance.
int dist = str.charAt(0) - 'a';

Step 2: shift all characters through the same distance.
for (char c : char_array) 
    buffer.append((c - 'a' - dist + 26) % 26 + 'a');
Note there is trick for this. Since 'c' - 'a' may be a negative number, we plus 26 to make it positive.
Note: to use the extra range wayaround, we also need to minus 'a'.


(c - 'a' - dist + 26) % 26 + 'a'
We first make the character c have the index in the range [0 , 25] : c - 'a'.
Then we shift he character in the range through minus dist: c - 'a' - dist.
To avoid negative situation, we plus 26 after it. (since the range is 26, it would have no effect over positive number).
The we take mod of 26 for positive case (which exceeds 26).
The we convert it back to ASCII range.


Solution:

copy code
public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        if (strings == null)
            throw new IllegalArgumentException("strings is null");
        List<List<String>> ret = new ArrayList<List<String>> ();
        if (strings.length == 0)
            return ret;
        HashMap<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>> ();
        for (String str : strings) {
            String shifted_str = shiftStr(str);
            if (map.containsKey(shifted_str)) {
                map.get(shifted_str).add(str);
            } else{
                ArrayList<String> item = new ArrayList<String> ();
                item.add(str);
                map.put(shifted_str, item);
                ret.add(item);
            }
        }
        for (List<String> list : ret)
            Collections.sort(list);
        return ret;
    }


    private String shiftStr(String str) {
        StringBuffer buffer = new StringBuffer();
        char[] char_array = str.toCharArray();
        int dist = str.charAt(0) - 'a';
        for (char c : char_array) 
            buffer.append((c - 'a' - dist + 26) % 26 + 'a');
        return buffer.toString();
    }
}
    
