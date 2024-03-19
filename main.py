from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the maximum element in each sliding window of size k in the given array.

        Args:
            nums: The input array of integers.
            k: The size of the sliding window.

        Returns:
            A list of integers representing the maximum element in each sliding window.
        """
        n = len(nums)
        result = []
        window = deque()

        # Process the first k elements of the array
        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)

        # Process the remaining elements of the array
        for i in range(k, n):
            result.append(nums[window[0]])

            # Remove the leftmost element if it's outside the current window
            if window and window[0] <= i - k:
                window.popleft()

            # Remove the elements smaller than the current element from the right
            while window and nums[i] >= nums[window[-1]]:
                window.pop()

            window.append(i)

        # Append the maximum element of the last window
        result.append(nums[window[0]])

        return result