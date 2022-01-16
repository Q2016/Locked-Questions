class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cooldown=1;
        
        int buy[prices.size()];
        int sell[prices.size()];
        memset(buy, 0, sizeof(buy));
        memset(sell, 0, sizeof(sell));
        buy[0] = -prices[0];
        for(int i=1; i<prices.size(); i++) {
            buy[i] = max(buy[i-1], (i-cooldown-1 >= 0 ? sell[i-cooldown-1] : 0) - prices[i]);
            sell[i] = max(sell[i-1],prices[i] + buy[i-1]);
        }
        return max(sell[prices.size()-1], buy[prices.size()-1]);
    }
};
