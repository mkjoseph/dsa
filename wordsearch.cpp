
#include <vector>
#include <string>

# https://leetcode.com/problems/word-search/
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (search(board, visited, i, j, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    bool search(vector<vector<char>>& board, vector<vector<bool>>& visited, int i, int j, int index, string& word) {
        if (index == word.length()) {
            return true;
        }
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || board[i][j] != word[index]) {
            return false;
        }
        visited[i][j] = true;
        bool found = search(board, visited, i + 1, j, index + 1, word) ||
                     search(board, visited, i - 1, j, index + 1, word) ||
                     search(board, visited, i, j + 1, index + 1, word) ||
                     search(board, visited, i, j - 1, index + 1, word);
        visited[i][j] = false;
        return found;
    }
};
