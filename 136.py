def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test the function
nums = [2, 2, 1]
print(singleNumber(nums))  # Output: 1

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4

nums = [1]
print(singleNumber(nums))  # Output: 1


# Pass 2 