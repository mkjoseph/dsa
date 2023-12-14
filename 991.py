def brokenCalc(startValue: int, target: int) -> int:
    operations = 0
    
    while target > startValue:
        if target % 2 == 0:
            target //= 2
        else:
            target += 1
        operations += 1
    
    return operations + startValue - target


# Pass 2 
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2: target += 1
            else: target //= 2

        return ans + startValue - target