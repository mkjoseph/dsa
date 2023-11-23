/**
 * @class Solution
 * @brief Class that calculates the largest rectangle area in a given histogram.
 */
/**
 * @class Solution
 * @brief Class that calculates the largest rectangle area in a given histogram.
 */
class Solution {
    private:
    /**
     * @brief Calculates the indices of the next smaller element for each element in the array.
     * @param arr The input array.
     * @param n The size of the array.
     * @return A vector containing the indices of the next smaller element for each element in the array.
     */
    vector<int> nextSmallerElement(vector<int>arr,int n){
        stack<int>s;
        s.push(-1);
        vector<int>ans(n);
        for(int i=n-1;i>=0;i--){
            int curr=arr[i];
        while(s.top()!=-1&& arr[s.top()]>=curr){
            s.pop();
        }
        ans[i]=s.top();
        s.push(i);
        }
        return ans;
    }
    
    /**
     * @brief Calculates the indices of the previous smaller element for each element in the array.
     * @param arr The input array.
     * @param n The size of the array.
     * @return A vector containing the indices of the previous smaller element for each element in the array.
     */
     vector<int> prevSmallerElement(vector<int>arr,int n){
        stack<int>s;
        s.push(-1);
        vector<int>ans(n);
        for(int i=0;i<n;i++){
            int curr=arr[i];
        while(s.top()!=-1&&arr[s.top()]>=curr){
            s.pop();
        }
        ans[i]=s.top();
        s.push(i);
        }
        return ans;
    }
public:
    /**
     * @brief Calculates the largest rectangle area in a given histogram.
     * @param heights The input histogram represented as an array of heights.
     * @return The largest rectangle area in the histogram.
     */
    int largestRectangleArea(vector<int>& heights) {
        int n=heights.size();
        vector<int>next(n);
        next=nextSmallerElement(heights,n);
        vector<int>prev(n);
        prev=prevSmallerElement(heights,n);
        int area=INT_MIN;
        for(int i=0;i<n;i++){
        int length=heights[i];
        if(next[i]==-1){
            next[i]=n;
        }
        int breadth=next[i]-prev[i]-1;
        int newArea=length*breadth;
        area=max(area,newArea);
        }
        return area;
    }
};