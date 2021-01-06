class Solution {
public:
    int numberOfMatches(int n) {
        if (n == 0 || n == 1)
        {return 0;}
        if (n == 2)
        {return 1;}
        int j = 0;
        while (n > 2)
        {
            int i = (n%2==0)?n/2:n/2+1;
            j = n/2 + j;
            n = i;
        }
        return j + 1;
    }
};