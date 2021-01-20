class Solution {
public:
    static bool cmp(pair<char, int>& a, pair<char, int>& b) {
        return a.second > b.second;
    }

    string mysort(unordered_map<char, int>& unmap ) {
        vector<pair<char, int> > V;
        string str;
        for (auto &elem : unmap ) {
            V.push_back(elem);
        }
        sort(V.begin(), V.end(), cmp);
        for (auto& elem : V) {
            for (int i = 0; i < elem.second; ++i) {
                str += elem.first;
            }
        }
        return str;
    }

    string frequencySort(string s) {
        string ans;
        unordered_map<char, int > unmap;
        for (int i = 0; i < s.size(); ++i) {   
            unmap[ s[i] ] += 1;
        }
        ans = mysort(unmap);
        return ans;
    }
};
