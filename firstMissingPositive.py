# First pass
def firstMissingPositive(nums):
    """
    Find the smallest missing positive integer in an unsorted array.

    Args:
    nums (List[int]): The input array.

    Returns:
    int: The smallest missing positive integer.

    Time Complexity: O(n)
    Space Complexity: O(1) - constant extra space
    """
    n = len(nums)

    # Segregate positive numbers and non-positive numbers
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = float('inf')  # Replace non-positive numbers with infinity

    # Mark elements as visited
    for i in range(n):
        val = abs(nums[i])
        if 1 <= val <= n:
            nums[val - 1] = -abs(nums[val - 1])

    # Find the smallest missing positive integer
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1

# Example usage
nums = [3, 4, -1, 1]
print("The smallest missing positive integer is:", firstMissingPositive(nums))





# Second pass