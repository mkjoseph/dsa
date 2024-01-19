// 1. Brute Force
// Class named Solution
class Solution {

    // Method that returns an array of integers, taking a 2D array 'intervals' as input
    public int[] findRightInterval(int[][] intervals) {
        // 'res' is an array to store the result, sized to the length of 'intervals'
        int[] res = new int[intervals.length];

        // Loop through each interval
        for (int i = 0; i < intervals.length; i++) {
            // 'min' is used to find the minimum starting point of the right interval
            int min = Integer.MAX_VALUE;
            // 'minindex' stores the index of the interval with the minimum starting point
            int minindex = -1;

            // Nested loop to compare the current interval with all others
            for (int j = 0; j < intervals.length; j++) {
                // Check if the start of the j-th interval is after or at the end of the i-th interval
                // and if it is smaller than the current 'min'
                if (intervals[j][0] >= intervals[i][1] && intervals[j][0] < min) {
                    // Update 'min' and 'minindex' with the new minimum values
                    min = intervals[j][0];
                    minindex = j;
                }
            }

            // Store the index of the right interval for the i-th interval in the result array
            res[i] = minindex;
        }

        // Return the resulting array
        return res;
    }
}

// 2: Using Sorting + Scanning
// Class named Solution
class Solution {

    // Method that returns an array of integers, taking a 2D array 'intervals' as input
    public int[] findRightInterval(int[][] intervals) {
        // 'res' is an array to store the result, sized to the length of 'intervals'
        int[] res = new int[intervals.length];
        
        // A HashMap to store each interval and its original index
        Map<int[], Integer> hash = new HashMap<>();

        // Loop to populate the HashMap with intervals and their original indices
        for (int i = 0; i < intervals.length; i++) {
            hash.put(intervals[i], i);
        }

        // Sorting the intervals array based on the starting points of intervals
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // Loop through each interval
        for (int i = 0; i < intervals.length; i++) {
            // 'min' is used to find the minimum starting point of the right interval
            int min = Integer.MAX_VALUE;
            // 'minindex' stores the index of the interval with the minimum starting point
            int minindex = -1;

            // Nested loop to compare the current interval with remaining intervals
            for (int j = i; j < intervals.length; j++) {
                // Check if the start of the j-th interval is after or at the end of the i-th interval
                // and if it is smaller than the current 'min'
                if (intervals[j][0] >= intervals[i][1] && intervals[j][0] < min) {
                    // Update 'min' and 'minindex' with the new minimum values
                    min = intervals[j][0];
                    minindex = hash.get(intervals[j]);
                }
            }

            // Store the index of the right interval for the i-th interval in the result array
            // Using the original index from the HashMap
            res[hash.get(intervals[i])] = minindex;
        }

        // Return the resulting array
        return res;
    }
}
