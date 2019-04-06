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
    bool HasSubtree(TreeNode* p1, TreeNode* p2)
    {
        if(p1==nullptr || p2==nullptr)
            return false;
        if(p2->left == nullptr && p2->right == nullptr)
            return false;
        if(p1->left == nullptr && p1->right == nullptr)
            return false;
        if (p1->val == p2->val)
            if(equalTree(p1->left, p2->left) && equalTree(p1->right, p2->right))
                return true;
        return HasSubtree(p1->left, p2) || HasSubtree(p1->right, p2);
    }
    
    bool equalTree(TreeNode* p1,TreeNode* p2)
    {
        if(p1==nullptr && p2==nullptr)
            return true;
        if (p1==nullptr || p2==nullptr)
            return false;
        if(p2->left == nullptr && p2->right == nullptr && p1->val == p2->val)
            return true;
        if(p1->left == nullptr && p1->right == nullptr)
            return false;
        if (p1->val == p2->val)
            return equalTree(p1->left, p2->left) && equalTree(p1->right, p2->right);
        return false;
    }
};
