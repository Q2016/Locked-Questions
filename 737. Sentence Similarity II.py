Question:
Given two sentences words1, words2 (each represented as an array of strings), 
and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] 
are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
Note that the similarity relation is transitive. For example, if “great” and “good” are
similar, and “fine” and “good” are similar, then “great” and “fine” are similar.
Similarity is also symmetric. For example, “great” and “fine” being similar is the same 
as “fine” and “great” being similar.
Also, a word is always similar with itself. For example, the sentences words1 = ["great"], 
words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
Finally, sentences can only be similar if they have the same number of words. So a sentence 
like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].









Solution: (The solution gives the general idea)
https://medium.com/@rebeccahezhang/leetcode-737-sentence-similarity-ii-2ca213f10115
    
This is more complicated than Sentence Similarity I. To check if two words are similar 
given the transitivity (for example If “A” = “B”, “B” = “C”, then “A” = “C”), we can use 
a graph to help us connect all similar words together. Then for each word pairs, we start 
from the source word, using DFS to find the destination word. In case of we do DFS to the 
same node twice, we can create a set to keep a record of visited nodes.
Let’s walk through a simple example:
words1 = [“A”, “B”, “C”], words2 = [“D”, “E”, “F”]
pairs[][] = [“A”, “G”],[“D”, “G”],[“B”, “E”],[“C”, “F”]
We construct the graph using a map to represent it.
String |set<String>
A | [G]
G | [A, D]
D | [G]
B | [E]
E | [B]
C | [F]
F | [C]
Now we begin to check A and D. A is the source, D is the target.
We go to the entry where the key is A, and check if this set contains D. It doesn’t,
but contains G! It’s possible G has a set contains D, so we change our source from A 
to G and keep finding out. We get the set [A, D], and we need to check each word here. 
The first one is A again, oh we just checked this! We don’t want to go to an endless loop. 
So we need to skip this, and we see D. It’s equal to the target! We are done. Well, on the 
opposite, if we are not this lucky, we need to keep finding. After we go through the entire 
map we still can’t find the target, we failed.


class Solution {
    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, String[][] pairs) {
        if (words1.length != words2.length) {
            return false;
        }
        // Build the graph of pairs
        HashMap<String, Set<String>> pairMap = new HashMap<>();
        for (String[] pair : pairs) {
            // Create keys(words in [][]pairs without duplication) and empty set 
            if (!pairMap.containsKey(pair[0])) {
                pairMap.put(pair[0], new HashSet<String>());
            }
            if (!pairMap.containsKey(pair[1])) {
                pairMap.put(pair[1], new HashSet<String>());
            }
            // Add the corresponding pairs to each other
            pairMap.get(pair[0]).add(pair[1]);
            pairMap.get(pair[1]).add(pair[0]);
        }
     
        // Iterate throught each word in both input strings and do DFS search
        for (int i = 0; i < words1.length; i++) {
            // If same, then we don't need to do DFS search
            if (words1[i].equals(words2[i])) continue;
            // If they are not the same and no such strings in the pairs
            if (!pairMap.containsKey(words1[i]) || !pairMap.containsKey(words2[i])) return false;
            // Do DFS search, initialize the set to prevent revisiting. 
            if (!dfs(words1[i], words2[i], pairMap, new HashSet<>())) return false;
        }
        return true;
    }
        
    public boolean dfs(String source, String target, HashMap<String, Set<String>> pairMap, HashSet<String> visited) {
        if (pairMap.get(source).contains(target)) {
            return true;
        }
        // Mark as visited 
        visited.add(source);
        for (String next : pairMap.get(source)) {
            // DFS other connected node, except the mirrowed string 
            if (!visited.contains(next) && next.equals(target) ||
                !visited.contains(next) && dfs(next, target, pairMap, visited)) {
                return true;    
            }
        }
        // We've done dfs still can't find the target 
        return false;
    }
}
      



