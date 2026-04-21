// Last updated: 4/21/2026, 11:27:15 PM
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
#include <queue>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(root == NULL){
            return {};
        }
        queue<TreeNode*> q;
        vector<vector<int>> zigzag;
        int flag = 0;
        
        q.push(root);
        TreeNode* curr;
        
        while(!q.empty()){
            int size = q.size();
            vector<int> level(size);
           
            for(int i = 0; i < size; i++){
                curr = q.front();
                q.pop();
                
                int index = flag ? size - 1 - i: i;
                level[index] = curr->val;
                if ( curr-> left ) q.push(curr->left);
                if ( curr->right ) q.push(curr->right);
            }
        zigzag.push_back(level);
        flag = !flag;
        }
        return zigzag;
    }
};