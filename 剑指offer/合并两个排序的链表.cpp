/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode* temp;
        ListNode* result1 = pHead1, *result2 = pHead2;
        if(pHead1==nullptr)
            return pHead2;
        if(pHead2==nullptr)
            return pHead1;
        while(pHead1!=nullptr && pHead2!=nullptr)
        {
            while(pHead1->val>=pHead2->val)
            {
                if(pHead2->next!=nullptr)
                {
                    if (pHead1->val<=pHead2->next->val)
                    {
                        temp = pHead2->next;
                        pHead2->next=pHead1;
                        pHead2 = temp;
                        break;
                    }
                    pHead2 = pHead2->next;
                }
                else
                {
                    pHead2->next = pHead1;
                    return result1->val>=result2->val?result2:result1;
                }
            }
            while(pHead1->val<=pHead2->val)
            {
                if(pHead1->next!=nullptr)
                {
                    if (pHead2->val<=pHead1->next->val)
                    {
                        temp = pHead1->next;
                        pHead1->next=pHead2;
                        pHead1 = temp;
                        break;
                    }
                    pHead1 = pHead1->next;
                }
                else
                {
                    pHead1->next = pHead2;
                    return result1->val>=result2->val?result2:result1;
                }
            }
        }
        return result1->val>result2->val?result2:result1;
    }
};
