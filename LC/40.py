# pass 1 

def combination_sum2(candidates, target):
  results = []
  candidates.sort()  # Sorting avoids some duplicate checks

  def backtrack(curr, pos, remaining):
      if remaining == 0:
          results.append(curr.copy())
      elif remaining < 0:
          return

      prev = -1  # To handle duplicates
      for i in range(pos, len(candidates)):
          # Avoid duplicates 
          if candidates[i] == prev:
              continue
          curr.append(candidates[i])
          backtrack(curr, i + 1, remaining - candidates[i])  # Note: i + 1 for single use
          curr.pop()
          prev = candidates[i]

  backtrack([], 0, target)
  return results


# pass 2 
def combination_sum2_iterative(candidates, target):
results = []
candidates.sort()

stack = [([], 0, target)]  # (combination, index, remaining_target)
while stack:
    curr, pos, remaining = stack.pop()

    if remaining == 0:
        results.append(curr)
        continue

    prev = -1
    for i in range(pos, len(candidates)):
        if candidates[i] == prev:
            continue
        if remaining - candidates[i] < 0:
            break  # Optimization: Prune search branch

        stack.append((curr + [candidates[i]], i + 1, remaining - candidates[i]))
        prev = candidates[i]

return results


# pass 3 

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

result = combination_sum2(candidates, target)  # Using the recursive backtracking solution
print(result)  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]] 
