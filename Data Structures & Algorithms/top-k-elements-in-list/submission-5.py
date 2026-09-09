class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        faiz = {}

        for num in nums :
            faiz[num]=faiz.get(num,0)+1

        bucket=[[] for i in range(len(nums)+1)]

        for num , freq in faiz.items():
            bucket[freq].append(num)

        result = []

        for freq in  range(len(bucket)-1,0,-1) :
            for num in bucket[freq]:
                result.append(num)

                if len(result)==k:
                    return result





        
            
                                                
        