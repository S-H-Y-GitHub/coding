/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool f(TreeNode* p1, TreeNode* p2)
    {
        if(p1==nullptr && p2 ==nullptr)
            return true;
        if(p1!=nullptr && p2 !=nullptr)
            return p1->val==p2->val && f(p1->left, p2->right) && f(p1->right, p2->left);
        return false;
    }
    bool isSymmetrical(TreeNode* p)
    {
        TreeNode *p1, *p2;
        if(p!=nullptr)
        {
            p1=p->left;
            p2=p->right;
            return f(p1, p2);
        }
        return true;
    }

};
