def subarraysWithKDistinct(nums, k):

  def atMostKDistinct(k):
    count = 0
    left = 0
    freq = {}
    for right in range(len(nums)):
      if nums[right] not in freq or freq[nums[right]] == 0:
        k -= 1
      freq[nums[right]] = freq.get(nums[right], 0) + 1

      while k < 0:
        freq[nums[left]] -= 1
        if freq[nums[left]] == 0:
          k += 1
        left += 1

      count += right - left + 1
    return count

  return atMostKDistinct(k) - atMostKDistinct(k - 1)


# Commenting out the function call as per instructions
# print(subarraysWithKDistinct([1,2,1,2,3], 2))
# print(subarraysWithKDistinct([1,2,1,3,4], 3))
