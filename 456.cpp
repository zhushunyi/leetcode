claclass Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int two = INT_MIN;
        stack<int> st;
        for(int i = nums.size()-1; i>=0; i--){
            if(nums[i] < two) return true; 
            while(!st.empty() && nums[st.top()] < nums[i]){
                two = nums[st.top()]; 
                st.pop();
            }
            st.push(i);
        }
        return false;
    }
};