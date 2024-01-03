def dailyTemperatures(temperatures):
    n = len(temperatures)
    stack = []
    answer = [0] * n

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    return answer


#Pass 2 

def dailyTemperatures(self, T):
    """
    Calculates the number of days you have to wait until a warmer temperature is found for each day.

    Args:
        T (List[int]): A list of daily temperatures.

    Returns:
        List[int]: A list of integers representing the number of days you have to wait until a warmer temperature is found for each day.
    """
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)

    return ans
