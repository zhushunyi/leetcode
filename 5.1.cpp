/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head, *temp=&head;
        while(l1!=NULL && l2!=NULL)
        {
            if (l1->val<=l2->val)
            {
                cout << 1 << endl;
                temp->next=l1;
                l1=l1->next;
            }
            else
            {
                cout << 2 << endl;
                temp->next=l2;
                l2=l2->next;
            }
            temp=temp->next;
        }
        temp->next = l1 == nullptr ? l2 : l1;
        return head.next;
        
    }
};