
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        water += (left_max - height[left]) * (height[left] >= height[right]) or (right_max - height[right]) * (height[left] < height[right])
        left, right = left + (height[left] >= height[right]), right - (height[left] >= height[right])
    return water
