class Solution {
public:
    int minCount(vector<int>& coins) {
        int n = coins.size();
        int cnt = 0;
        int i = 0;
        while (i < n)
        {
            int temp = (coins[i]%2 == 0)? (coins[i]/2):(coins[i]/2 + 1);
            cnt = cnt + temp;
            ++i;
        }
        return cnt;
    }
};