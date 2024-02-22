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

# PASS 2


class Solution:

  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

    def count_subarrays(max_distinct):
      """Counts the subarrays with at most 'max_distinct' distinct integers"""
      left = 0
      distinct_count = 0
      counts = collections.Counter()
      subarray_count = 0

      for right, num in enumerate(nums):
        counts[num] += 1
        if counts[num] == 1:
          distinct_count += 1

        # Shrink window until we have 'max_distinct' distinct integers
        while distinct_count > max_distinct:
          counts[nums[left]] -= 1
          if counts[nums[left]] == 0:
            distinct_count -= 1
          left += 1

        # At this point, the window from 'left' to 'right' has at most
        # 'max_distinct' distinct integers
        subarray_count += right - left + 1

      return subarray_count

    return count_subarrays(k) - count_subarrays(k - 1)
