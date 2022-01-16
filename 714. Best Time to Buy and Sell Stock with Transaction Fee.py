class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int sell[prices.size()];
        int buy[prices.size()];
        memset(sell,0,sizeof(sell));
        memset(buy,0,sizeof(buy));
        buy[0] = -prices[0];
        for(int i=1; i<prices.size();i++) {
            buy[i] = max(buy[i-1], sell[i-1] - prices[i]);
            sell[i] = max(sell[i-1],prices[i] + buy[i-1] - fee);
        }
        return max(buy[prices.size()-1],sell[prices.size()-1]);
    }
};
