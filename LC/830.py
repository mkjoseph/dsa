def largeGroupPositions(self, S):
    i, j, N = 0, 0, len(S)
    res = []
    while i < N:
        while j < N and S[j] == S[i]: j += 1
        if j - i >= 3: res.append([i, j - 1])
        i = j
    return res

# pass 2

# finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the RE pattern in string. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.

 return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]