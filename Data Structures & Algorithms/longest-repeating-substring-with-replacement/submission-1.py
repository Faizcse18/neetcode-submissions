class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        faiz = {}

        l,r = 0,0
        longest=0

        while r <len(s):
            faiz[s[r]]=faiz.get(s[r],0)+1

            while (r-l)+1 - max(faiz.values())>k:
                faiz[s[l]]-=1
                l+=1

            longest=max(longest,r-l+1)
            r+=1

        return longest

            

      



        