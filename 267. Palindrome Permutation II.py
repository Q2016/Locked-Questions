Problem:
Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

If a palindromic permutation exists, we just need to generate the first half of the string.

# Time:  O(n * n!)
# Space: O(n)

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())
        return self.permuteUnique(mid, chars) if len(mid) < 2 else []
    
    def permuteUnique(self, mid, nums):
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(mid, result, used, [], nums)
        return result
    
    def permuteUniqueRecu(self, mid, result, used, cur, nums):
        if len(cur) == len(nums):
            half_palindrome = ''.join(cur)
            result.append(half_palindrome + mid + half_palindrome[::-1])
            return
        for i in xrange(len(nums)):
            if not used[i] and not (i > 0 and nums[i-1] == nums[i] and used[i-1]):
                used[i] = True
                cur.append(nums[i])
                self.permuteUniqueRecu(mid, result, used, cur, nums)
                cur.pop()
                used[i] = False

class Solution2(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = tuple(k for k, v in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())
        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []
    
    
    
    
    
    
or:
    
    
    class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        odd = None
        for k, v in m.items():
            if v % 2 == 1:
                if odd is not None:
                    return []
                odd = k

        cur = ""
        if odd:
            m[odd] -= 1
            cur = odd

        ret = []
        # actually only need to build half
        self.grow(s, m, None, cur, ret)
        return ret

    def grow(self, s, count_map, pi, cur, ret):
        if len(cur) == len(s):
            ret.append(cur)
            return

        for k in count_map.keys():
            if k != pi and count_map[k] > 0:
                for i in xrange(1, count_map[k]/2+1):  # jump the parent
                    count_map[k] -= i*2
                    self.grow(s, count_map, k, k*i+cur+k*i, ret)
                    count_map[k] += i*2
