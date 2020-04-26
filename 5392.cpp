class Solution {
public:
    int maxScore(string s) {
        int length = s.size();
        int a[length];
        int temp = 0;
        for (int i = 0; i < length; ++i)
        {
            if (s[i] == '1')
            {++temp;}
            a[i] = temp;
        }
        int maximum = 0;
        /*for (auto i:a)
        {
            cout << i << endl;
        }*/
        for (int i = 0; i < length-1; ++i)
        {
            maximum = max(maximum,i+1+temp-2*a[i]);
        }
        return maximum;
    }
};