import math

def constructRectangle(area):
    """
    Constructs a rectangle with the given area.

    Parameters:
    area (int): The area of the rectangle.

    Returns:
    list: A list containing the length and width of the rectangle.
    """
    width = int(math.sqrt(area))
    while area % width != 0:
        width -= 1
    length = area // width
    return [length, width]


#pass 2

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for l in range(int(area**0.5), 0, -1):            
            if area % l == 0: 
                return [area // l, l]