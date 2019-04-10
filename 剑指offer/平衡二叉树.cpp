class Solution {
public:
    bool IsBalanced_Solution(TreeNode* p) {
        return IsBalanced_Solution2(p)!=-1;
    }
    int IsBalanced_Solution2(TreeNode* p) {
        int l, r;
        if (p==nullptr)
            return 0;
        l=IsBalanced_Solution2(p->left);
        r=IsBalanced_Solution2(p->right);
        if(l!=-1 && r!=-1 && l-r<=1 && r-l<=1)
            return r>l?r+1:l+1;
        else
            return -1;
    }
};
