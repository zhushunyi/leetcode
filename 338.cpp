class Solution {
public:
    vector<int> countBits(int num) {
        //O(n*sizeof(integer))
        /*
        vector<int> ans;
        ans.push_back(0);
        int i = 1;
        while (i < num+1)
        {
            int j = i;
            int temp = 0;
            while (j != 0)
            {
                if (j%2 == 1)
                {++temp;}
                j = j/2;
            }
            ans.push_back(temp);
            ++i;
        }
        return ans;*/

        vector<int> ans(num+1);
        ans[0] = 0;
        for(int i = 1; i <= num; i++)
        {
            if(i % 2 == 1)
            {
                ans[i] = ans[i-1] + 1;
            }
            else
            {
                ans[i] = ans[i/2];
            }
        }       
        return ans;
    }
};