Question:
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time 
(in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.


Example 1:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same 
name and is in a different city. Similarly the second one is invalid too.










Solution: Brute force

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        length = len(transactions)
        if not length: return ans
        name,time,money,city = [],[],[],[]
        add = [1]*length
        for trans in transactions:
            tran = trans.split(',')
            name.append(tran[0])
            time.append(eval(tran[1]))
            money.append(eval(tran[2]))
            city.append(tran[3])
        for i in range(length):
            if money[i] > 1000:
                add[i] = False
            for j in range(i+1,length):
                if name[i] == name[j] and abs(time[i]-time[j])<= 60 and city[i]!=city[j]:
                    add[i] = False
                    add[j] = False
        for ind,val in enumerate(add):
            if not val:
                ans.append(transactions[ind])
        return ans
        
        
        
Time O(N^2)



Approach 2: 


class Solution(object):
    def invalidTransactions(self, transactions):
        
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: [city]
                }
            else:
                if name not in r[time]:
                    r[time][name]=[city]
                else:
                    r[time][name].append(city)
                    
        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                if len(r[j][name]) > 1 or (r[j][name][0] != city):
                    inv.append(i)
                    break
                                        
        return inv
