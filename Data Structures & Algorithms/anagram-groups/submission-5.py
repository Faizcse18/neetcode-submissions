class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}

        for i in strs:
            faiz = "".join(sorted(i))

            if faiz not in anas:
                anas[faiz] = []

            anas[faiz].append(i)

        return list(anas.values())
        

        