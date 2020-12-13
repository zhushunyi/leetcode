class Solution {
public:
    static int cmp ( const void *a , const void *b )
{
    return *(int *)a - *(int *)b;
}

    vector<int> sortedSquares(vector<int>& nums) {
        int i = nums.size();
        //cout << i << endl;
        vector<int> vec(i);
        for (int j = 0; j < i; ++j)
        {
            vec[j] = nums[j]*nums[j];
        }
        //sort(vec.begin(),vec.end());
        qsort(&vec[0],i,sizeof(int),cmp);
        return vec;
    }
};