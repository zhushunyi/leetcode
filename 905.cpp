class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int n = A.size();
        vector<int> arr1;
        vector<int> arr2;
        int i = 0;
        while(i < n)
        {
            if (A[i]%2 == 0)
            {arr1.push_back(A[i]);}
            else
            {arr2.push_back(A[i]);}
            ++i;
        }
        vector<int> ans;
        ans.insert(ans.end(),arr1.begin(),arr1.end());
        ans.insert(ans.end(),arr2.begin(),arr2.end());
        return ans;
    }
};