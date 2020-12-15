/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int depth(TreeNode* node)
    {
        if (node == NULL)
        {return 0;}
        int left = depth(node->left);
        int right = depth(node->right);
        return max(left,right)+1;
    }
    bool isBalanced(TreeNode* root) {
        if (root == NULL)
        {return true;}
        if (abs(depth(root->left) - depth(root->right)) < 2)
        {
            return isBalanced(root->left) && isBalanced(root->right);
        }
        return false;
    }
};