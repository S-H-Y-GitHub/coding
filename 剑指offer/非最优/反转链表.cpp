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
    ListNode* ReverseList(ListNode* pHead) {
        vector<int> temp;
        ListNode * result, * b;
        while(pHead!=nullptr)
        {
            temp.push_back(pHead->val);
            pHead=pHead->next;
        }
        if(temp.size() == 0)
            return nullptr;
        result = b = new ListNode(*(temp.end()-1));
        if(temp.size() == 1)
            return result;
        for (auto a=temp.end(); a!=temp.begin()+1; a--)
        {
            b->next = new ListNode(*(a-2));
            b = b->next;
        }
        return result;
    }
};
