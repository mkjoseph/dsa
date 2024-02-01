def largeGroupPositions(S):
  i, j, N = 0, 0, len(S)
  res = []
  while i < N:
    while j < N and S[j] == S[i]:
      j += 1
    if j - i >= 3:
      res.append([i, j - 1])
    i = j

  print(res)
  return res

# Call the function with a string that contains large groups
largeGroupPositions("pppddddkasdfn")
