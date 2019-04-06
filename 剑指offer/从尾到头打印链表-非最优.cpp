/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> rr,r;
        while(head!=NULL)
        {
            rr.push_back(head->val);
            head=head->next;
        }
        for(int i=rr.size()-1; i>=0; i--)
        {
            r.push_back(rr[i]);
        }
        return r;
    }
};
