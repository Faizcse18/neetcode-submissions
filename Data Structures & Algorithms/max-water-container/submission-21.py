class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r=0,len(heights)-1
        Max_area=0

        while l < r:
            width=r-l
            height=min(heights[l],heights[r])
            Area=width*height

            Max_area=max(Max_area,Area)

            if heights[l]<heights[r]:
                l+=1

            else:
                r-=1

        return Max_area

        