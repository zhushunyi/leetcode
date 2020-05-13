class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int length = nums.size();
        int i = 0;
        int temp;
        while (i < length)
        {
            temp = temp ^ nums[i];
            ++i;
        }
        return temp;

    }
};