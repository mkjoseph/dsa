#include <vector>

using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    bool isCol = false;
    int R = matrix.size();
    int C = matrix[0].size();
    for (int i = 0; i < R; i++) {
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        for (int j = 1; j < C; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    for (int i = 1; i < R; i++) {
        for (int j = 1; j < C; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    if (matrix[0][0] == 0) {
        for (int j = 0; j < C; j++) {
            matrix[0][j] = 0;
        }
    }
    if (isCol) {
        for (int i = 0; i < R; i++) {
            matrix[i][0] = 0;
        }
    }
}


// pass 2 
#include <vector>

using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    bool isCol = false;
    int R = matrix.size(), C = matrix[0].size();

    // Use first row and column as markers, set isCol if first column needs to be zeroed
    for (int i = 0; i < R; i++) {
        if (matrix[i][0] == 0) isCol = true;
        for (int j = 1; j < C; j++) {
            if (matrix[i][j] == 0) matrix[i][0] = matrix[0][j] = 0;
        }
    }

    // Iterate over the matrix and using the first row and column, update the elements
    for (int i = 1; i < R; i++) {
        for (int j = 1; j < C; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
        }
    }

    // Update first row if needed
    if (matrix[0][0] == 0) {
        fill(matrix[0].begin(), matrix[0].end(), 0);
    }

    // Update first column if needed
    if (isCol) {
        for (int i = 0; i < R; i++) matrix[i][0] = 0;
    }
}


