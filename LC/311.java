// Pass 1 
public class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        int m = A.length, n = A[0].length, nB = B[0].length;
        int[][] C = new int[m][nB];

        for(int i = 0; i < m; i++) {
            for(int k = 0; k < n; k++) {
                if (A[i][k] != 0) {
                    for (int j = 0; j < nB; j++) {
                        if (B[k][j] != 0) C[i][j] += A[i][k] * B[k][j];
                    }
                }
            }
        }
        return C;   
    }
}
/*
Efficiency: Optimized by checking if A[i][k] != 0 and B[k][j] != 0 before multiplication, which avoids unnecessary calculations.
Clarity: Straightforward nested loop structure makes the code easily understandable.
Potential Improvement: Lack of comments might make it harder for others to quickly grasp the logic, especially for complex matrix operations.
 */

// Pass 2 
public int[][] multiply(int[][] A, int[][] B) {
    int m = A.length, n = A[0].length, nB = B[0].length;
    int[][] result = new int[m][nB];

    List[] indexA = new List[m];
    for(int i = 0; i < m; i++) {
        List<Integer> numsA = new ArrayList<>();
        for(int j = 0; j < n; j++) {
            if(A[i][j] != 0){
                numsA.add(j); 
                numsA.add(A[i][j]);
            }
        }
        indexA[i] = numsA;
    }

    for(int i = 0; i < m; i++) {
        List<Integer> numsA = indexA[i];
        for(int p = 0; p < numsA.size() - 1; p += 2) {
            int colA = numsA.get(p);
            int valA = numsA.get(p + 1);
            for(int j = 0; j < nB; j ++) {
                int valB = B[colA][j];
                result[i][j] += valA * valB;
            }
        }
    }

    return result;   
}

/*
 * Optimization: Utilizes a list to store non-zero elements and their indices from matrix A, which can reduce the number of multiplications.
Readability: This approach is slightly more complex than the first pass due to additional data structure manipulation. 
Inline comments explaining the logic would enhance readability.
Potential Issue: Using raw type for List[] indexA is not a best practice in Java. 
Prefer using generics for type safety, e.g., List<List<Integer>>.
Maintainability: This approach is less intuitive and might be harder to maintain or modify by other developers without adequate documentation.
 */

// Summation

/*
 * Pass 1:

Pros: Simplicity and efficiency in cases of sparse matrices.
Cons: Could be improved with comments for clarity.
Pass 2:

Pros: Potentially more efficient for very sparse matrices.
Cons: Complexity, lack of generics, and reduced maintainability.
Overall, Pass 1 is preferable for its simplicity and readability, 
especially if the efficiency gain in Pass 2 is marginal for the expected input matrices. 
However, for extremely sparse matrices, Pass 2 could offer performance benefits. 
In both cases, adding comments would greatly aid in understanding the code.
 */

// brute

public int[][] multiply_bruteForce(int[][] A, int[][] B) {
	int m = A.length, n = A[0].length;
	int nB = B[0].length;
	int [][] C = new int[m][nB];
	for (int i = 0; i<m; i++) {
		for (int j = 0; j<nB; j++){
			C[i][j] = 0;
			for( int k = 0; k<n; k++)
				C[i][j] += A[i][k]*B[k][j];
		}
	}
	return C;
}