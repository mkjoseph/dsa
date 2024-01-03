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

def singleNumber(self, nums: List[int]) -> int:
	return reduce(lambda total, el: total ^ el, nums)

# Pass 3

def singleNumber(self, nums: List[int]) -> int:
    return (x := 0, [x := x ^ v for v in nums])[-1][-1]