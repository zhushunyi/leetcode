class MinStack {
public:
    /** initialize your data structure here. */
    int mini=INT_MAX;
    stack<int> stk;

    MinStack() {
        cerr<<1<<endl;
        
    }
    
    void push(int x) {
        stk.push(x);
        if (x<=mini)
        {mini=x;}
        cerr<<"push"<<endl;
    }
    
    void pop() {
        if (mini!=stk.top())
        {stk.pop();
        cerr<<1<<endl;}
        else
        {
            stk.pop();
            if (!stk.empty())
            {stack<int>temp;
            mini=stk.top();
            while(!stk.empty())
            {
                mini=min(mini,stk.top());
                temp.push(stk.top());
                stk.pop();
            }
            while(!temp.empty())
            {
                stk.push(temp.top());
                temp.pop();
            }
            cerr << 2 << endl;}
            else
            {mini=INT_MAX;}
        }
        
    }
    
    int top() {
        cerr << "top" << endl;
        return stk.top();
    }
    
    int getMin() {
        cerr<<"min"<<endl;
        return mini;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */