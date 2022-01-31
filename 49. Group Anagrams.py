Question:
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word 
or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]    


Question:
    
    def groupAnagrams(self, strs):

        anagrams_map, result = collections.defaultdict(list), []
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_map[sorted_str].append(s)
        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)
        return result

    
# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)
