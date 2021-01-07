class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ret;
        int i = 0;
        while (i < n)
        {
            ++i;
            if (i%15 == 0)
            {
                ret.push_back("FizzBuzz");
                continue;
            }
            if (i%3 == 0)
            {
                ret.push_back("Fizz");
                continue;
            }
            if (i%5 == 0)
            {
                ret.push_back("Buzz");
                continue;
            }
            ret.push_back(to_string(i));
        }
        return ret;
    }
};