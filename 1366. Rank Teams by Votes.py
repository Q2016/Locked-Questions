Question:
In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.
The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, 
we consider the second position to resolve the conflict, if they tie again, we continue this process until 
the ties are resolved. If two or more teams are still tied after considering all positions, 
we rank them alphabetically based on their team letter. Given an array of strings votes which is the votes of all voters in 
the ranking systems. Sort all teams according to the ranking system described above.
Return a string of all teams sorted by the ranking system.
 
Example 1:
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
Team B was ranked second by 2 voters and was ranked third by 3 voters.
Team C was ranked second by 3 voters and was ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team and team B is the third.    



Solution: sort and dic
    
Steps
Create a ranking system for each char of each string in the array (hashmap), s.t.:

	d = {
		'A': [0, 0, 0],  # initialize array of size len(string)
		'B': [0, 0, 0],
		...
	}
For each char in the string, we add 1 to the position they are ranked,
e.g. d['A'] = [3, 0, 1] means A is ranked first 3 times, second 0 times, and third once.

Sort d.keys() based on their ranking values in dictionary, in descending order
in case of equal votes, we alphabetically order the keys first using .sort()

Join elements in the sorted list into a string

Complexity
time: O(N * S + N logN) ~ O(N logN)
space: O(N * S) ~ O(N)
where N = # votes and S = length of a word in the votes array
max(S) is 26 chars so it would be constant O(1)

Python3
    def rankTeams(self, votes: List[str]) -> str:
        d = {}

        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1

          #output for d: {'A': [5, 0, 0], 'B': [0, 2, 3], 'C': [0, 3, 2]}
           
        voted_names = sorted(d.keys()) 
        # output for dict_keys(['A', 'B', 'C'])
        # voted_names output: ['A', 'B', 'C']
        
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))

       
       
       
       
Complexity
Time O(NM) for iterating
Time O(MMlogM) for sorting
Space O(M^2)
where N = votes.length and M = votes[0].length <= 26


C++

    string rankTeams(vector<string>& votes) {
        vector<vector<int>> count(26, vector<int>(27));
        for (char& c: votes[0])
            count[c - 'A'][26] = c;

        for (string& vote: votes)
            for (int i = 0; i < vote.length(); ++i)
                --count[vote[i] - 'A'][i];
        sort(count.begin(), count.end());
        string res;
        for (int i = 0; i < votes[0].length(); ++i)
            res += count[i][26];
        return res;
    }
       
