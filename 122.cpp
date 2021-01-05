class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int i = 0;
        int profit = 0;
        while (i < n - 1)
        {
            profit = max(profit,profit + prices[i+1]-prices[i]);
            ++i;
        };
        return profit;
        
    }
};