#first pass
def min_window_substring(s, t):
    # Count the occurrences of characters in t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Initialize variables for the sliding window approach
    start, end = 0, 0
    min_length = float('inf')
    min_window = ""
    required = len(t_count)
    formed = 0
    window_counts = {}

    while end < len(s):
        # Add one character from the right to the window
        char = s[end]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'
        while start <= end and formed == required:
            char = s[start]

            # Update the result if this window is smaller than the previously found minimum
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_window = s[start:end+1]

            # Remove characters from the left and update the count in the window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            start += 1    

        end += 1

    return min_window

# Test the function with an example
s = "ADOBECODEBANC"
t = "ABC"
min_window_substring(s, t)


# 2nd pass
def found_target(target_len):
    return target_len == 0

class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
			# If we see a target letter, decrease the total target letter count
			if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve
			target_letter_counts[search_string[end]] -= 1
            
			# If all letters in the target are found:
            while found_target(target_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				# Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window