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
