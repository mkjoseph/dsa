// Include Directives and Namespaces

#include <vector>
#include <string>

# https://leetcode.com/problems/word-search/
using namespace std;

class Solution {
public:
    // public member function that checks if a word exists in a given 2D board.
    bool exist(vector<vector<char>>& board, string word) {
            // Dimensions of the board
        int m = board.size();
        int n = board[0].size();
        // visited = 2D vector to track visited positions on the board
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
    // private helper function used by exist to perform a depth-first search
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
