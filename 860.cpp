class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int n = bills.size();
        int five = 0;
        int ten = 0;
        int i = 0;
        while (i < n)
        {
            if (bills[i] == 5)
            {
                ++five;
            }
            if (bills[i] == 10)
            {
                if (five > 0)
                {
                    --five;
                    ++ten;
                }
                else
                {return false;}
            }
            if (bills[i] == 20)
            {
                if (five > 0 && ten > 0)
                {
                    --five;
                    --ten;
                    ++i;
                    continue;
                }
                else if (five > 2)
                {
                    five = five - 3;
                    ++i;
                    continue;
                }
                else
                {return false;}
            }
            ++i;
        }
        return true;

    }
};