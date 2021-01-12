class CQueue {
private:

stack<int> stk1;
stack<int> stk2;

public:
    CQueue() {
    }
    
    void appendTail(int value) {
        stk1.push(value);
        return;

    }
    
    int deleteHead() {
        if (stk1.empty() && stk2.empty())
        {return -1;}
        if (stk2.empty())
        {
            while (!stk1.empty())
            {
                int temp = stk1.top();
                stk1.pop();
                stk2.push(temp);
            }
        }
        int ans = stk2.top();
        stk2.pop();
        return ans;
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */