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
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* res = new TreeNode(-1);
        TreeNode* temp = res;
        stack<TreeNode*> arr;
        TreeNode* node = root;

        while(node != nullptr) {
            arr.push(node);
            node = node->left;
        }

        while(!arr.empty()) {
            node = arr.top();
            arr.pop();
            temp->right = new TreeNode(node->val);
            temp = temp->right;
            if(node->right != nullptr) {
                node = node->right;
                while(node != nullptr) {
                    arr.push(node);
                    node = node->left;
                }
            }
        }
        return res->right;

    }
};
