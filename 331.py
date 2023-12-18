def isValidSerialization(preorder: str) -> bool:
    """
    Check if a given preorder traversal of a binary tree is valid.

    Args:
        preorder (str): The preorder traversal of the binary tree.

    Returns:
        bool: True if the preorder traversal is valid, False otherwise.
    """
    stack = []
    nodes = preorder.split(',')

    for node in nodes:
        stack.append(node)

        while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('#')

    return len(stack) == 1 and stack[0] == '#'


# Pass 2 
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot
        
        p = preorder.split(',')
        
        #initially we have one empty slot to put the root in it
        slot = 1
        for node in p:
            
            # no empty slot to put the current node
            if slot == 0:
                return False
                
            # a null node?
            if node == '#':
                # ocuppy slot
                slot -= 1
            else:
                # create new slot
                slot += 1
        
        #we don't allow empty slots at the end
        return slot==0
    
# Pass 3

'''
public boolean isValidSerialization(String preorder) {
    String[] nodes = preorder.split(",");
    int diff = 1;
    for (String node: nodes) {
        if (--diff < 0) return false;
        if (!node.equals("#")) diff += 2;
    }
    return diff == 0;
}
'''

def is_valid_serialization(preorder: str) -> bool:
    """
    Check if the given preorder serialization of a binary tree is valid.

    A valid serialization is one where each non-null node provides exactly two child nodes
    and each null node (represented by '#') does not provide any child nodes.

    Args:
    preorder (str): A string representing the preorder serialization of a binary tree,
                    where nodes are separated by commas.

    Returns:
    bool: True if the serialization is valid, False otherwise.
    """
    nodes = preorder.split(",")
    diff = 1  # Initial diff for the root node.

    for node in nodes:
        diff -= 1  # Decrease for visiting a node.
        if diff < 0:
            return False
        if node != "#":
            diff += 2  # Increase for two children if the node is not null.

    return diff == 0

# Example usage
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(is_valid_serialization(preorder))  # Output: True or False based on the input
