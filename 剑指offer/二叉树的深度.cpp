/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    int TreeDepth(TreeNode* p)
    {
        int l,r;
        if(p==nullptr)
            return 0;
        l=TreeDepth(p->left);
        r=TreeDepth(p->right);
        if(l>r)
            return l+1;
        else
            return r+1;
    }
};
