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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        vector<int> result;
        vector<TreeNode*> tmp;
        auto p1=0, p2=0;
        if(root!=nullptr)
            tmp.push_back(root);
        while(p1<tmp.size())
        {
            for(;p1<tmp.size();p1++)
                result.push_back((tmp[p1])->val);
            for(;p2<p1;p2++){
                if((tmp[p2])->left!=nullptr)
                    tmp.push_back((tmp[p2])->left);
                if((tmp[p2])->right!=nullptr)
                    tmp.push_back((tmp[p2])->right);
            }
        }
        return result;
    }
};
