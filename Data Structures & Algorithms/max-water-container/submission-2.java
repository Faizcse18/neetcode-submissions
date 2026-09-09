class Solution {
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length-1;
        int area = 0;
        int maxArea = Integer.MIN_VALUE;

        while(left < right) {
            int width = right - left;
            int height = Math.min(heights[left], heights[right]);
            area = height * width;
            maxArea = Math.max(area, maxArea);
            if(heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
