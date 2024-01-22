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

// 3. Sorting + Binary Search
public class Solution {

    // Method to perform binary search on the intervals
    public int[] binary_search(int[][] intervals, int target, int start, int end) {
        // Base condition for recursion - if start index is greater than or equal to end index
        if (start >= end) {
            // Check if the current interval's start is greater than or equal to target
            if (intervals[start][0] >= target) {
                return intervals[start];
            }
            // Return null if no suitable interval is found
            return null;
        }

        // Calculate the middle index
        int mid = (start + end) / 2;

        // If the middle interval's start is less than the target, search in the right half
        if (intervals[mid][0] < target) {
            return binary_search(intervals, target, mid + 1, end);
        } else {
            // Else, search in the left half
            return binary_search(intervals, target, start, mid);
        }
    }

    // Method to find the right interval for each interval in the list
    public int[] findRightInterval(int[][] intervals) {
        // Result array to store indices of the right intervals
        int[] res = new int[intervals.length];

        // HashMap to store each interval and its original index
        HashMap<int[], Integer> hash = new HashMap<>();

        // Populating the HashMap with intervals and their original indices
        for (int i = 0; i < intervals.length; i++) {
            hash.put(intervals[i], i);
        }

        // Sorting the intervals based on their starting points
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // Loop through each interval
        for (int i = 0; i < intervals.length; i++) {
            // Perform binary search to find the right interval for the current interval
            int[] interval = binary_search(intervals, intervals[i][1], 0, intervals.length - 1);

            // Store the result using the original index, -1 if no interval is found
            res[hash.get(intervals[i])] = interval == null ? -1 : hash.get(interval);
        }

        // Return the result array
        return res;
    }
}

// 4. TreeMap
public class Solution {

    // Method to find the right interval for each interval in the list
    public int[] findRightInterval(int[][] intervals) {
        // A TreeMap to store the starting points of intervals and their indices
        TreeMap<Integer, Integer> starts = new TreeMap<>();

        // Result array to store indices of the right intervals
        int[] res = new int[intervals.length];

        // Loop to populate the TreeMap with the starting points and their indices
        for (int i = 0; i < intervals.length; i++) {
            starts.put(intervals[i][0], i);
        }

        // Loop through each interval
        for (int i = 0; i < intervals.length; i++) {
            // Find the least starting point greater than or equal to the end point of the current interval
            Map.Entry<Integer, Integer> pos = starts.ceilingEntry(intervals[i][1]);

            // Store the index of the right interval in the result array, -1 if no such interval exists
            res[i] = pos == null ? -1 : pos.getValue();
        }

        // Return the result array
        return res;
    }
}


// 5. Two Arrays w/o Binary Search
public class Solution {

    // Method to find the right interval for each interval in the list
    public int[] findRightInterval(int[][] intervals) {
        // Creating a copy of intervals to separately sort by end times
        int[][] endIntervals = Arrays.copyOf(intervals, intervals.length);

        // HashMap to store each interval and its original index
        HashMap<int[], Integer> hash = new HashMap<>();

        // Loop to populate the HashMap with intervals and their original indices
        for (int i = 0; i < intervals.length; i++) {
            hash.put(intervals[i], i);
        }

        // Sorting the intervals based on their starting points
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // Sorting the copied intervals based on their ending points
        Arrays.sort(endIntervals, (a, b) -> a[1] - b[1]);

        // 'j' is a pointer used for iterating through the intervals
        int j = 0;

        // Array to store indices of the right intervals
        int[] res = new int[intervals.length];

        // Loop through each interval sorted by end time
        for (int i = 0; i < endIntervals.length; i++) {
            // Increment 'j' until finding an interval that starts after the current interval ends
            while (j < intervals.length && intervals[j][0] < endIntervals[i][1]) {
                j++;
            }

            // Store the index of the right interval in the result array
            // If 'j' reaches the end, store -1 indicating no right interval was found
            res[hash.get(endIntervals[i])] = j == intervals.length ? -1 : hash.get(intervals[j]);
        }

        // Return the result array
        return res;
    }
}


/*
 * Copying Arrays: endIntervals is created as a copy of intervals to sort intervals based on their end times.
HashMap: A HashMap (hash) stores each interval and its original index. This helps in retrieving the original index after sorting.
Sorting: The original intervals array is sorted by start times, and endIntervals is sorted by end times.
Iterating with Two Pointers: The variable j is used to iterate through the sorted intervals, and i iterates through endIntervals.
Finding Right Interval: The while loop increments j to find the first interval in intervals that starts after the end of the current interval in endIntervals.
Storing Results: The index of the right interval is stored in res. If no such interval is found (when j reaches the length of intervals), -1 is stored.
Returning the Array: The method returns the res array, which contains the indices of the right intervals for each interval in endIntervals, according to their original order in intervals.
 */
