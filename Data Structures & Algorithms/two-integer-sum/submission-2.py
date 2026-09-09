class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wajeeha={}

        for i , num in enumerate(nums):
            faiz = target - num

            if faiz in wajeeha :
                return[wajeeha[faiz],i]

            wajeeha[num]=i
        