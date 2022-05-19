Question:
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array 
'fruits' where 'fruits[i]' is the type of fruit the 'ith' tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

    
    
Solution: sliding window
    
Another way of saying this:    
What is the length of longest subarray that contains up to two distinct integers?
longest-substring-with-at-most-two-distinct-characters

Problem
"Start from any index, we can collect at most two types of fruits. What is the maximum amount"


Translation
Find out the longest length of subarrays with at most 2 different numbers?


Explanation
Solve with sliding window,
and maintain a hashmap counter,
which count the number of element between the two pointers.
Find more infinite similar prolems in the end.


Complexity
Time O(n)
Space O(1)


    def totalFruit(self, tree):
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1
