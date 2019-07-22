/*
中序遍历的循环写法
可以减少额外空间values的使用，改成k--
*/

class Solution {
public:
   TreeNode* KthNode(TreeNode* pRoot, int k)
   {
      stack<TreeNode*> s = stack<TreeNode*>();
      vector<TreeNode*> values = vector<TreeNode*>();
      TreeNode* p = pRoot;
      s.push(pRoot);
      if (pRoot == nullptr)
         return nullptr;
      while (!s.empty())
      {
         while (p->left != nullptr)
         {
            s.push(p->left);
            p = p->left;
         }

         while (!s.empty())
         {
            p = s.top();
            s.pop();
            values.push_back(p);
            if (values.size() == k)
               return p;
            if (p->right != nullptr)
            {
               s.push(p->right);
               p = p->right;
               break;
            }
         }
      }
      return values[k-1];
   }
};
