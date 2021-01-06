class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        int n = prices.size();
        if (n == 0 || n == 1)
        {return prices;}
        vector<int> ans;
        stack<int> stk;
        int temp;
        for (int i = 0; i < n - 1; ++i)
        {
            temp = prices[i];
            for (int j = i+1; j < n; ++j)
            {
                if (prices[j] <= prices[i])
                {
                    temp = prices[i] - prices[j];
                    break;
                }
            }
            ans.push_back(temp);
        }
        ans.push_back(prices[n-1]);
        return ans;
    }
};s