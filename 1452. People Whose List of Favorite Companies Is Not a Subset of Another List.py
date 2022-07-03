Question:
Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies 
for the ith person (indexed from 0). Return the indices of people whose list of favorite companies 
is not a subset of any other list of favorites companies. You must return the indices in increasing order.

Example 1:
Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4] 
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of 
favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of 
favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].    


Solution:
    
https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/discuss/636512/Python3-Easy-Solution

Thanks to Python set library

    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        d = {i: set(v) for i, v in enumerate(A)}
        res = []
        for i in range(len(A)):
            subSet = True
            for j in range(len(A)):
                if i == j:
                    continue
                if not d[i] - d[j]: # below
                    subSet = False
                    break
            if subSet: res.append(i)         
        return res  
    
it removes the elements from d[i] if it is also present in d[j], gives the remaining elements in d[i] as answer
for example
d[i]={1,2,5}
d[j]={2,5,7,8}
d[i]-d[j]={1}
d[j]-d[i]={7,8}    

Time complexity:
    
    Analysis:

Let
m = favoriteCompanies.size(),
a = average size of all companies (favoriteCompanies[0].size() + favoriteCompanies[1].size() + .. + favoriteCompanies[m - 1].size()) / m,
b = average size of company names.

There needs O(m * a * b) time and O(m * a) space to create all sets, and there are O(m ^ 2) iterations due to the nested for loops, 
and each check for subset relation cost time O(a). Therefore:

Time: O(m * a * (m + b)), space: O(m * a).
