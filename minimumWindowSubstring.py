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
