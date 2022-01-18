Approach #1: Cartesian Product [Accepted]
Intuition and Algorithm

For each place to put the comma, we separate the string into two fragments. For example, with a string like "1234", we could separate it into fragments "1" and "234", "12" and "34", or "123" and "4".

Then, for each fragment, we have a choice of where to put the period, to create a list make(...) of choices. For example, "123" could be made into "1.23", "12.3", or "123".

Because of extranneous zeroes, we should ignore possibilities where the part of the fragment to the left of the decimal starts with "0" (unless it is exactly "0"), and ignore possibilities where the part of the fragment to the right of the decimal ends with "0", as these are not allowed.

Note that this process could result in an empty answer, such as for the case S = "(000)".

Example 1:

Input: s = "(123)"
Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
Example 2:

Input: s = "(0123)"
Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
Explanation: 0.0, 00, 0001 or 00.01 are not allowed.
Example 3:

Input: s = "(00011)"
Output: ["(0, 0.011)","(0.001, 1)"]

  class Solution(object):
    def ambiguousCoordinates(self, S):
        def make(frag):
            N = len(frag)
            for d in xrange(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in xrange(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]
