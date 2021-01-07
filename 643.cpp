class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        double ans = 0;
        double temp = 0;
        for (int i = 0; i < k; ++i)
        {
            ans = ans + nums[i];
            temp = ans;
        }
        for (int i = 1; i < n + 1 - k; ++i)
        {
            temp = temp - nums[i-1] + nums[i+k-1];
            ans = max(ans,temp);
        }
        return ans/k;
    }
};