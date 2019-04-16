/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
        
    }
};
*/
class Solution {
public:
    TreeLinkNode* GetNext(TreeLinkNode* p)
    {
        if(p==nullptr)
            return p;
        if (p->right != nullptr)
        {
            p=p->right;
            while(p->left!=nullptr)
                p=p->left;
            return p;
        }
            
        while(p->next != nullptr && p->next->right == p)
            p=p->next;
        
        return p->next;
            
    }
};
