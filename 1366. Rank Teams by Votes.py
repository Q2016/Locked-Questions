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



Solution: ---
    
Count the rank of vote for each candidate. Sort all teams according to the ranking system.


def rankTeams(votes: List[str]) -> str:
    counter = {k:[0]*len(votes[0]) for k in votes[0]}

    for val in votes:
        for i,ch in enumerate(val):
            counter[ch][i]-=1 # - as we need to sort in reverse
    sorted_counter = sorted(counter.items(), key=lambda k:(k[1],k[0]))
    ans = ""
    for ch,_ in sorted_counter:
        ans+=ch
    return ans
