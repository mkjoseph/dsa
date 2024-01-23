// pass 1


public class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }
    
    private int pathSumFrom(TreeNode node, int sum) {
        if (node == null) return 0;
        return (node.val == sum ? 1 : 0) 
            + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val);
    }
}

// notes

// Definition of the Solution class
public class Solution {

    // Public method pathSum which takes the root of a binary tree and an integer sum
    // Returns the total number of paths that sum to the given value.
    public int pathSum(TreeNode root, int sum) {
        // If the root is null, there are no paths, so return 0.
        if (root == null) return 0;

        // The total number of paths is the sum of:
        // 1. Paths starting from the current root node.
        // 2. Paths from the left subtree.
        // 3. Paths from the right subtree.
        return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }
    
    // Private helper method to count paths starting from a given node that sum to the given value.
    private int pathSumFrom(TreeNode node, int sum) {
        // If the node is null, return 0 as there are no paths.
        if (node == null) return 0;

        // The total number of paths from this node is:
        // 1. 1, if the node's value equals the remaining sum.
        // 2. The number of paths from the left child with the updated sum.
        // 3. The number of paths from the right child with the updated sum.
        return (node.val == sum ? 1 : 0) 
            + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val);
    }
}

// TreeNode class is assumed to be defined elsewhere.
// It typically includes at least a value field and left/right child references.

