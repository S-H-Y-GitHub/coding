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
    void Mirror(TreeNode *p) {
        if(p==nullptr)
            return;
        TreeNode *t = p->left;
        p->left = p->right;
        p->right = t;
        Mirror(p->left);
        Mirror(p->right);
    }
};
