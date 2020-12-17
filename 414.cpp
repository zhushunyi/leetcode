class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int n = nums.size();
        if (n == 1)
        {
            return nums[0];
        }
        if (n == 2)
        {
            return (nums[0] < nums[1])? nums[1]:nums[0];
        }
        vector<int> vec;
        vec.push_back(nums[0]);
        int i = 1;
        int j = 1;
        while (j < 3)
        {
            if (j == 1 && nums[i] != vec[0])
            {
                vec.push_back(nums[i]);
                ++i;
                ++j;
            }
            else if (j == 1 && nums[i] == vec[0])
            {
                ++i;
            }
            else if (j == 2 && nums[i] != vec[0] && nums[i] != vec[1])
            {
                vec.push_back(nums[i]);
                ++i;
                ++j;
            }
            else
            {++i;}
            if (i == n)
            {break;}
        }
        while (i < n)
        {
            auto minimum = min_element(begin(vec),end(vec));
            if (nums[i] > *minimum && nums[i]!=vec[0] && nums[i]!=vec[1] && nums[i]!=vec[2])
            {
                vec[distance(begin(vec),minimum)] = nums[i];
            }
            ++i;
        }
        n = vec.size();
        if (n == 1)
        {
            return vec[0];
        }
        if (n == 2)
        {
            return (vec[0] < vec[1])? vec[1]:vec[0];
        }
        auto minimum = min_element(begin(vec),end(vec));
        return *minimum;
    }
};