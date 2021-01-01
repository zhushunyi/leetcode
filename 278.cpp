// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
    int low = 1;
    int high = n;
    while (low < high) {
        // will cause overflow
        // int temp = (temp + high)/2;
        int temp = low + (high - low) / 2;
        if (isBadVersion(temp)) {
            high = temp;
        } else {
            low = temp + 1;
        }
    }
    return low;
    }
};