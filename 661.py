def imageSmoother(img):
    m, n = len(img), len(img[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            total = 0
            count = 0
            for x in range(max(0, i-1), min(m, i+2)):
                for y in range(max(0, j-1), min(n, j+2)):
                    total += img[x][y]
                    count += 1
            result[i][j] = total // count
    
    return result


#Pass 2

from copy import deepcopy

class Solution(object):
    """
    Class to perform image smoothing on a given matrix.
    """

    def imageSmoother(self, M):
        """
        Smooths the given image matrix by calculating the average of each pixel's neighbors.

        :param M: The image matrix represented as a list of lists.
        :type M: List[List[int]]
        :return: The smoothed image matrix.
        :rtype: List[List[int]]
        """
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = deepcopy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res