# Pass 1 

def pathSum(root, targetSum):
    def dfs(node, path, path_sum):
        if not node:
            return
        
        path.append(node.val)
        path_sum += node.val
        
        if not node.left and not node.right and path_sum == targetSum:
            result.append(path[:])
        
        dfs(node.left, path, path_sum)
        dfs(node.right, path, path_sum)
        
        path.pop()
        path_sum -= node.val
    
    result = []
    dfs(root, [], 0)
    return result

# Pass 2 -------------------

'''

To solve this problem, you can use a depth-first search (DFS) approach to traverse the binary tree and keep track of the path sum. When a leaf node is reached (a node with no children), check if the sum of the path equals the target sum. If it does, add that path to the list of valid paths. Here's how you can implement this in Python:

Define a class TreeNode to represent each node in the binary tree.
Create a helper function that performs DFS on the tree.
Accumulate the path nodes and their sum while traversing.
Check at each leaf if the accumulated sum equals the target sum, and if so, add the path to the result.


The TreeNode class represents a node in the binary tree.
The pathSum function initiates the DFS traversal.
The dfs function is a helper function that traverses the tree, keeps track of the path and its sum, and adds valid paths to the result list.
Finally, the pathSum function returns the list of all valid paths.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(node, current_sum, path):
        if not node:
            return

        current_sum += node.val
        path.append(node.val)

        # Check if the current node is a leaf and the current sum equals targetSum
        if not node.left and not node.right and current_sum == targetSum:
            result.append(list(path))

        # Continue to explore the left and right children
        dfs(node.left, current_sum, path)
        dfs(node.right, current_sum, path)

        # Backtrack to explore other paths
        path.pop()

    result = []
    dfs(root, 0, [])
    return result

# Example usage
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(pathSum(root, 22))  # Output: [[5, 4, 11, 2], [5, 8, 4, 5]]


# Pass++ 

def pathSum(self, root, sum):
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, ls, res):
        if root:
			if not root.left and not root.right and sum == root.val:
				ls.append(root.val)
				res.append(ls)
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
            self.dfs(root.right, sum-root.val, ls+[root.val], res)
            
    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]
    
    # BFS + queue    
    def pathSum3(self, root, sum): 
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
        
    # DFS + stack I  
    def pathSum4(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 
    
    # DFS + stack II   
    def pathSum5(self, root, s): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res