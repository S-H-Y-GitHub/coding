//todo：写法比较差，可以直接递归
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int pre_i = -1;
    
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        if(vin.size() == 0)
            return NULL;
        pre_i++;
        TreeNode* root = new TreeNode((pre.at(pre_i)));
        //forgotten how to use c++ find()
        int i=-1;
        while(i!=vin.size())
        {
            i++;
            if(vin[i]==pre.at(pre_i))
                break;
        }
        
        if (i!=vin.size())
        {
            root->left = reConstructBinaryTree(pre,vector<int>(vin.begin(),vin.begin()+i));
            root->right = reConstructBinaryTree(pre,vector<int>(vin.begin()+i+1,vin.end()));
            return root;
        }
        return NULL;
    }
};
