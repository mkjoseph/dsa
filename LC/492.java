import java.util.ArrayList;
import java.util.List;

public class RectangleConstructor {
    
    // Approach 1: Function
    public static List<Integer> constructRectangle(int area) {
        int width = (int) Math.sqrt(area);
        while (area % width != 0) {
            width--;
        }
        int length = area / width;
        List<Integer> result = new ArrayList<>();
        result.add(length);
        result.add(width);
        return result;
    }

    // Approach 2: Method within a class
    static class Solution {
        public List<Integer> constructRectangle(int area) {
            for (int l = (int) Math.sqrt(area); l > 0; l--) {
                if (area % l == 0) {
                    List<Integer> result = new ArrayList<>();
                    result.add(area / l);
                    result.add(l);
                    return result;
                }
            }
            return null; // This line will never be reached in the current logic
        }
    }

    // Test the code
    public static void main(String[] args) {
        List<Integer> rectangle1 = constructRectangle(4);
        System.out.println("Approach 1: " + rectangle1);

        Solution solution = new Solution();
        List<Integer> rectangle2 = solution.constructRectangle(4);
        System.out.println("Approach 2: " + rectangle2);
    }
}
