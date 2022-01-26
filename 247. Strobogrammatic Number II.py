Question:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example: 
Given n = 2, return ["11","69","88","96"].



Solution:

Recursion: T(n) = append each string with ("1", "1"); ("6","9"); ("9","6"); ("8","8"); 
if not at the out-most recursion; also add ("0","0") from returned element from T(n - 2); 
Base case: (n =0 => ['']; n = 1=>['0', '1', '8'])
Without Recursion: reverse the order with for loop

    def findStrobogrammatic(self, n):

        def helper(cur_len, total_len):
            # base case 
            if cur_len == 0: return ['']
            if cur_len == 1: return ['0', '1', '8']
            ans = []
            sub = helper(cur_len - 2, total_len)

            for s in sub:
                if cur_len != total_len:
                    ans.append("0" + s + "0")
                ans.append("1" + s + "1")
                ans.append("6" + s + "9")
                ans.append("8" + s + "8")
                ans.append("9" + s + "6")
            return ans

        return helper(n, n)
                
                
# Time:  O(n^2 * 5^(n/2))
# Space: O(n)                




