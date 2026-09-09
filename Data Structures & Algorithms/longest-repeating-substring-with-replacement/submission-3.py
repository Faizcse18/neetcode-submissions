class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        faiz={}
        l=0
        longest=0
        for r in range(len(s)):
            faiz[s[r]]=faiz.get(s[r],0)+1
            while (r-l+1)-max(faiz.values())>k:
                faiz[s[l]]-=1
                l+=1

            longest=max(longest,r-l+1)

        return longest



                






            

      



        