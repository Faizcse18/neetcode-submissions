class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        faiz ={}

        for i , num in enumerate(nums):
            anas = target- num

            if anas in faiz:
                return[faiz[anas],i]

            faiz[num] = i
        