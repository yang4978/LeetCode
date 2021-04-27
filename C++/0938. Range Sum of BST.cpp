/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        queue<TreeNode*> q;
        q.push(root);
        int res = 0;

        while(!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if(node->val >= low && node->val <= high) {
                res += node->val;
                if(node->left != nullptr) {
                    q.push(node->left);
                }
                if(node->right != nullptr) {
                    q.push(node->right);
                }
            } else if (node->val < low && node->right != nullptr) {
                q.push(node->right);
            } else if (node->val > high && node->left != nullptr) {
                q.push(node->left);
            }
        }
        return res;

    }
};
