 

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
        // Get the lengths of the input strings.
        int m = word1.size(), n = word2.size();
        
        // Create a 2D vector for dynamic programming, initialized with zeros.
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Initialize the first column of the dp matrix.
        for (int i = 1; i <= m; i++) {
            dp[i][0] = i; // Number of insertions required to convert word1 to an empty string.
        }
        
        // Initialize the first row of the dp matrix.
        for (int j = 1; j <= n; j++) {
            dp[0][j] = j; // Number of insertions required to convert an empty string to word2.
        }
        
        // Fill in the dp matrix using dynamic programming.
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]; // Characters match, no edit required.
                } else {
                    // Minimum of insertion, deletion, and substitution, plus 1.
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
            }
        }
        
        // Return the minimum edit distance stored in the last cell of dp.
        return dp[m][n];
    }
};
