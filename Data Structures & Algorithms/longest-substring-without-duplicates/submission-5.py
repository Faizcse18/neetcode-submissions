class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        faiz=set()
        l,r=0,0
        longest=0
        while r <len(s):
            
            while s[r] in faiz:
                faiz.remove(s[l])
                l+=1

            windows=r-l+1

            faiz.add(s[r])
            longest=max(longest,windows)
            r+=1

        return longest


        