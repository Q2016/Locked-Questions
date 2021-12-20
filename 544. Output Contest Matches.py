Problem:
During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

Example 1:

Input: 2
Output: (1,2)
Explanation: 
Initially, we have the team 1 and the team 2, placed like: 1,2.
Then we pair the team (1,2) together with '(', ')' and ',', which is the final answer.
Example 2:

Input: 4
Output: ((1,4),(2,3))
Explanation: 
In the first round, we pair the team 1 and 4, the team 2 and 3 together, as we need to make the strong team and weak team together.
And we got (1,4),(2,3).
In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner, so you need to add the paratheses outside them.
And we got the final answer ((1,4),(2,3)).
Example 3:


Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation: 
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
Note:

The n is in range [2, 2^12].
We ensure that the input n can be converted into the form 2^k, where k is a positive integer.
















https://protegejj.gitbook.io/algorithm-practice/google/544-output-contest-matches


(1) Iterative
思路: 就是像nba季后赛那样排名高的和对应的排名低的对位，每一轮的对位用括号包住，最后将所有轮次的对位用string表示出来。方法比较直接，就是先将1-n以string形式存入games这个长为n的数组，每一轮相当于将games[i]的string变成 "(" + games[i] + "," + games[round - i - 1] + ")", 因为每一轮是两队配对，所以在下一轮里面 n将减半，直到n等于1，输出结果
class Solution {
    public String findContestMatch(int n) {
        String[] games = new String[n];

        for (int i = 0; i < n; i++) {
            games[i] = String.valueOf(i + 1);
        }

        while (n > 1) {
            for (int i = 0; i < n / 2; i++) {
                games[i] = "(" + games[i] + "," + games[n - i - 1] + ")";
            }
            n /= 2;
        }
        return games[0];
    }
}
(2) Recursion
思路: 其实和iterative写法基本一样
class Solution {
    public String findContestMatch(int n) {
        String[] games = new String[n];

        for (int i = 0; i < n; i++) {
            games[i] = String.valueOf(i + 1);
        }

        findContestMatch(n , games);
        return games[0];
    }

    public void findContestMatch(int round, String[] games) {
        if (round == 1) return;

        for (int i = 0; i < round / 2; i++) {
            games[i] = "(" + games[i] + "," + games[round - i - 1] + ")";
        }

        findContestMatch(round / 2, games);
    }
}
3. Time & Space Complexity
(1) Iterative: 时间复杂度O(n), 空间复杂度O(n)
(2) Recursion: 时间复杂度O(n), 空间复杂度O(n）
