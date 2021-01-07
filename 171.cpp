class Solution {
public:
    int titleToNumber(string s) {
        int n = 0;
        int ans = 0;
        while (n < s.size())
        {
            ans = 26*ans + (s[n] - 'A' + 1);
            ++n;
        }
        return ans;
    }
};