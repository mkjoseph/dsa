# Pass 1 

def addToArrayForm(num, k):
    # Convert the array num into an integer
    num_int = int(''.join(map(str, num)))
    
    # Add k to the integer representation of num
    sum_int = num_int + k
    
    # Convert the sum back into an array
    sum_arr = []
    while sum_int > 0:
        sum_arr.insert(0, sum_int % 10)
        sum_int //= 10
    
    return sum_arr

# Pass 2 ------------------- 

def addToArrayForm(num, k):
    num = int(''.join(map(str, num)))  # Convert num array to an integer
    num += k  # Add k to the integer value of num
    return list(map(int, str(num)))  # Convert the sum back to an array of digits

# Test cases
print(addToArrayForm([1,2,0,0], 34))  # Output: [1,2,3,4]
print(addToArrayForm([2,7,4], 181))  # Output: [4,5,5]
print(addToArrayForm([2,1,5], 806))  # Output: [1,0,2,1]
