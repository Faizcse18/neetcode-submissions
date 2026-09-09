class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Faiz = set()
        for i in nums :
            if i in Faiz:
                return True
            Faiz.add(i)
        return False
        