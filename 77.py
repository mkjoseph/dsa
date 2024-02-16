# pass 1 
import itertools

def combine(n, k):
    return list(itertools.combinations(range(1, n + 1), k))


# pass 2 
def combine_recursive(n, k, start=1, curr=[]):
if len(curr) == k:
    return [curr.copy()]

res = []
for i in range(start, n + 1):
    res.extend(combine_recursive(n, k, i + 1, curr + [i]))
return res


# pass 3 

def combine_backtracking(n, k):
  res = []
  def backtrack(start, curr):
      if len(curr) == k:
          res.append(curr.copy())
          return

      for i in range(start, n + 1):
          curr.append(i)
          backtrack(i + 1, curr)
          curr.pop()

  backtrack(1, [])
  return res
