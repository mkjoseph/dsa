
# Pass 1

def isMatch(s: str, p: str) -> bool:
    # Create a 2D table to store the matching results
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*, etc.
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the table for all other cases
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[len(s)][len(p)]


# Pass 2 

'''
To implement regular expression matching that supports the '.' and '*' characters as described, you can use dynamic programming. The idea is to build a 2D table where each entry dp[i][j] represents whether the first i characters of the string s match the first j characters of the pattern p.

Let's define the rules for populating this table:

Initialization:

dp[0][0] = True, because an empty string matches an empty pattern.
dp[i][0] = False for all i > 0, because a non-empty string does not match an empty pattern.
dp[0][j] can be True if p[j-1] is '', and dp[0][j-2] is also True. This is because '' can represent zero occurrences of the preceding element.
Populating the Table:

For each i in 1 to len(s) and j in 1 to len(p):
If s[i-1] == p[j-1] or p[j-1] == '.', then dp[i][j] = dp[i-1][j-1]. This is because the current characters match, and we need to check the remaining part of the strings.
If p[j-1] == '*', then:
If p[j-2] matches s[i-1] or p[j-2] == '.', then dp[i][j] = dp[i][j-2] or dp[i-1][j]. This means '*' acts as multiple occurrences of p[j-2].
Else, dp[i][j] = dp[i][j-2]. This means '*' acts as zero occurrences of p[j-2].
Return Value:

The answer is dp[len(s)][len(p)], which represents whether the entire string s matches the entire pattern p.
'''


def isMatch(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(2, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] if p[j-2] == s[i-1] or p[j-2] == '.' else False)

    return dp[len(s)][len(p)]

'''
This function takes the input string s and the pattern p, and returns True if the pattern matches the entire string, or False otherwise. 
The use of dynamic programming makes it an efficient solution, particularly for cases where the pattern contains multiple '*' characters.
'''


# Pass 3

class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

'''

'''