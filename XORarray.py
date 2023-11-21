def bitwise_xor_of_array(n, start):
    """
    Calculate the bitwise XOR of an array where each element is defined as start + 2 * i.

    Args:
    n (int): The length of the array.
    start (int): The starting value for the array calculation.

    Returns:
    int: The result of the bitwise XOR of all elements in the array.
    """
    # Initialize the result with 0
    result = 0

    # Loop through the array and calculate the bitwise XOR
    for i in range(n):
        result ^= start + 2 * i

    return result

# Test the function with examples
if __name__ == "__main__":
    example1 = bitwise_xor_of_array(5, 0)  # Expected output: 8
    example2 = bitwise_xor_of_array(4, 3)  # Expected output: 8

    print(f"Example 1 Output: {example1}")
    print(f"Example 2 Output: {example2}")
