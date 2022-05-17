Question:
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended 
up with the string s.
For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".
Return a list of strings representing all possibilities for what our original coordinates could have been.
Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", 
or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit 
occurring before it, so we never started with numbers like ".1".
The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]

  
Solution: Cartesian Product [Accepted]
For each place to put the comma, we separate the string into two fragments. For example, with a string like "1234", we could separate it into 
fragments "1" and "234", "12" and "34", or "123" and "4".
Then, for each fragment, we have a choice of where to put the period, to create a list make(...) of choices. For example, "123" could be made 
into "1.23", "12.3", or "123".
Because of extranneous zeroes, we should ignore possibilities where the part of the fragment to the left of the decimal starts with "0" 
(unless it is exactly "0"), and ignore possibilities where the part of the fragment to the right of the decimal ends with "0", as these are not allowed.
Note that this process could result in an empty answer, such as for the case S = "(000)".



  class Solution(object):
    
    def ambiguousCoordinates(self, S):
      
        def make(frag):
            N = len(frag)
            for d in xrange(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0' and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand) for i in xrange(1, len(S)) for cand in itertools.product(make(S[:i]), make(S[i:]))]
