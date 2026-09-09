class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        
        Faiz = {}
        for i in s:
            Faiz[i]=Faiz.get(i,0) + 1

        for i in t :
            if i not in Faiz :
                return False

            Faiz[i]-=1

            if Faiz[i]<0:
                return False

        return True
