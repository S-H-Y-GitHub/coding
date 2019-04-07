//感觉是对的，但没办法debug
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
    struct TreeBlock{
        struct TreeNode *s;
	    struct TreeNode *l;
        TreeBlock(TreeNode *s, TreeNode *l):
            s(s),l(l){}
    };
    TreeNode* Convert(TreeNode* p)
    {
        if(p==nullptr)
            return p;
        return convertBlock(p)->s;
    }
    TreeBlock* convertBlock(TreeNode* p)
    {
        if(p==nullptr)
            return nullptr;
        TreeBlock* l = convertBlock(p->left);
        TreeBlock* r = convertBlock(p->right);
        TreeNode* x=p,*y=p;
        if(l!=nullptr)
        {
            l->l->right=p;
            p->left=l->l;
            x=l->s;
        }
        if(r!=nullptr)
        {
            p->right=r->s;
            r->s->right=p;
            y=r->l;
        }
        TreeBlock* result = new TreeBlock(x,y);
        delete l;
        delete r;
        return result;
    }
};
