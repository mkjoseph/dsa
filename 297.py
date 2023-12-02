








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
