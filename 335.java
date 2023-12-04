/**
 * This class represents a solution for determining if a given set of coordinates forms a self-crossing pattern.
 */
public class Solution {
    /**
     * Determines if the given set of coordinates forms a self-crossing pattern.
     *
     * @param x an array of integers representing the x-coordinates of the points
     * @return true if the coordinates form a self-crossing pattern, false otherwise
     */
    public boolean isSelfCrossing(int[] x) {
        // implementation code here
    }
}
public class Solution {
    public boolean isSelfCrossing(int[] x) {
        if (x.length <= 3) {
            return false;
        }
        int i = 2;
        // keep spiraling outward
        while (i < x.length && x[i] > x[i - 2]) {
            i++;
        }
        if (i >= x.length) {
            return false;
        }
        // transition from spiraling outward to spiraling inward
        if ((i >= 4 && x[i] >= x[i - 2] - x[i - 4]) ||
                (i == 3 && x[i] == x[i - 2])) {
            x[i - 1] -= x[i - 3];
        }
        i++;
        // keep spiraling inward
        while (i < x.length) {
            if (x[i] >= x[i - 2]) {
                return true;
            }
            i++;
        }
        return false;
    }
}

