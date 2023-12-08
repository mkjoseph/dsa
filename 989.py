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

