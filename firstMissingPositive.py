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

 def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n