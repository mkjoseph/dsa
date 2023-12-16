# Pass 1

def compareVersion(version1: str, version2: str) -> int:
    # Split the version numbers into revisions
    revisions1 = version1.split('.')
    revisions2 = version2.split('.')
    
    # Compare each revision from left to right
    for i in range(max(len(revisions1), len(revisions2))):
        # Get the integer value of each revision (or 0 if not specified)
        rev1 = int(revisions1[i]) if i < len(revisions1) else 0
        rev2 = int(revisions2[i]) if i < len(revisions2) else 0
        
        # Compare the revisions
        if rev1 > rev2:
            return 1
        elif rev1 < rev2:
            return -1
    
    # All revisions are equal
    return 0


# Pass 2 
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = list(map(int, v1.split('.'))), list(map(int, v2.split('.')))  
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                continue

            return -1 if rev1 < rev2 else 1 

        return 0

# Pass 3
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # the versions are equal
        return 0


