class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0)
        {return 1;}
        if (n == 1)
        {return 10;}
        int ret = 9;
        int temp = 9;
        int p = n;
        while (p > 1)
        {
            ret = ret * temp;
            --temp;
            --p;
        }
        cout << ret << endl;
        return (ret + countNumbersWithUniqueDigits(n-1));
    }
};