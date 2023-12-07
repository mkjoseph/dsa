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
