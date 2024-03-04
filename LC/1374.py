# version 0
    if n%2 == 0:
        return "a"*(n-1) + "b"
    else:
        return "a"*n

# version 1 
    def generateTheString(self, n):
        return 'b' + 'ab'[n & 1] * (n - 1)

# version 2 
return "a".repeat(n - 1) + ((n % 2 == 0)? "b" : "a");