Question:
Given a string s, return all the palindromic permutations (without duplicates) of it.

Example:
Given s = "aabb", return ["abba", "baab"].
Given s = "abc", return [].

Hint:
If a palindromic permutation exists, we just need to generate the first half of the string.


    def generatePalindromes(self, s):

        cnt = collections.Counter(s)
        mid = tuple(k for k, v in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())
        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []
    

# Time:  O(n * n!)
# Space: O(n)
