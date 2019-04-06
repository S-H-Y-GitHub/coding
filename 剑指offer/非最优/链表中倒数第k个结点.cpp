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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        vector<ListNode> temp;
        while(pListHead!=NULL)
        {
            temp.push_back(*pListHead);
            pListHead=pListHead->next;
        }
        if (k == 0)
            return nullptr;
        return temp.size()>=k?&temp[temp.size()-k]:nullptr;
    }
};
