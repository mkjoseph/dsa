# pass 1
class Solution(object):
def intersection(self, nums1, nums2):
    """
  
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))


# pass 2