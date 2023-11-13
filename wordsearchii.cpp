
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class TrieNode {
public:
    vector<TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : children(26, nullptr), isEndOfWord(false) {}
};
// creating a trie for the words in the dictionary


class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children[c - 'a']) {
                node->children[c - 'a'] = new TrieNode();
            }
            node = node->children[c - 'a'];
        }
        node->isEndOfWord = true;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie trie;
        for (string word : words) {
            trie.insert(word);
        }

        vector<string> result;
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, visited, "", i, j, trie.root, result);
            }
        }

        return result;
    }

private:
    void dfs(vector<vector<char>>& board, vector<vector<bool>>& visited, string word, int i, int j, TrieNode* node, vector<string>& result) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j]) {
            return;
        }

        char c = board[i][j];
        if (!node->children[c - 'a']) {
            return;
        }

        visited[i][j] = true;
        node = node->children[c - 'a'];
        word += c;
        if (node->isEndOfWord) {
            result.push_back(word);
            node->isEndOfWord = false; // avoid duplicates
        }

        dfs(board, visited, word, i + 1, j, node, result);
        dfs(board, visited, word, i - 1, j, node, result);
        dfs(board, visited, word, i, j + 1, node, result);
        dfs(board, visited, word, i, j - 1, node, result);

        visited[i][j] = false;
    }
};
