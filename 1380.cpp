class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> num1(m, INT_MAX);
        vector<int> num2(n, 0);
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                num1[i] = min(num1[i],matrix[i][j]);
                num2[j] = max(num2[j],matrix[i][j]);
            }
        }
        vector<int> num;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (num1[i] == num2[j]) {
                    num.push_back(matrix[i][j]);
                }
            }
        }

        return num;

    }
};