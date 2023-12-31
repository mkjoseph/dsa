'''

To serialize and deserialize a binary tree, you can use a method that traverses the tree in a specific order and represents it as a string. Here's one approach using a preorder traversal:

Serialize:

Start with an empty string to store the serialized tree.
Perform a preorder traversal of the binary tree.
For each node:
If the node is null, append "null," to the string.
Otherwise, append the node's value followed by a comma and space to the string.
Continue this process until all nodes have been processed.
Finally, return the serialized string.
Deserialize:

To deserialize the tree, split the serialized string by commas to get an array of values.
Initialize an index variable to keep track of the current position in the array.
Start building the tree recursively:
If the current value is "null," return null.
Otherwise, create a new TreeNode with the current value and increment the index.
Recursively call the deserialize function for the left and right children of the current node.
Return the root of the tree.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def preorder(node):
            if not node:
                serialized.append("null")
            else:
                serialized.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        
        serialized = []
        preorder(root)
        return ",".join(serialized)

    def deserialize(self, data):
        def build_tree():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
        
        values = iter(data.split(","))
        return build_tree()


# Alternative solution ------------------------------------------

class Codec:
    def serialize(self, root):
        """
        Serialize a binary tree to a string.
        
        Args:
            root (TreeNode): The root of the binary tree to be serialized.
            
        Returns:
            str: The serialized string representation of the binary tree.
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """
        Deserialize a string to a binary tree.
        
        Args:
            data (str): The serialized string representation of a binary tree.
            
        Returns:
            TreeNode: The root of the deserialized binary tree.
        """
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

