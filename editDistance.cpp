 

/**
 * @class Solution
 * @brief Class that calculates the minimum edit distance between two strings.
 */
class Solution {
public:
    /**
     * @brief Calculates the minimum edit distance between two strings.
     * @param word1 The first string.
     * @param word2 The second string.
     * @return The minimum edit distance between the two strings.
     */
    int minDistance(string word1, string word2) {
        // Implementation code...
    }
};
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 1; j <= n; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
            }
        }
        return dp[m][n];
    }
};