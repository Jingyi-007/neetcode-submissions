class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1
            
        sortbycount=sorted(count.items(),key=lambda x:x[1],reverse=True)
        pairs = sortbycount[:k]

        res = []
        for i in pairs :
            res.append(i[0])

        
        return res

                


