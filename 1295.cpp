class Solution {
public:
    int get_digit(int num)
    {
        int n = 1;
        while(num/10 != 0)
        {
            ++n;
            num = num/10;
        }
        if (n % 2 == 0)
        {
            return true;
        }
        return false;
    };

    int findNumbers(vector<int>& nums) {
        int n = nums.size();
        int j = 0;
        int i = 0;
        while (i < n)
        {
            if (get_digit(nums[i]))
            {
                ++j;
            }
            ++i;
        }
        return j;

    }
};