class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = {}

        for num in nums:
            my_hash[num] = my_hash.get(num, 0) + 1
        
        n = len(nums)
        buckets = [[]for _ in range(n + 1)]

        for num, freq in my_hash.items():
            buckets[freq].append(num) 

        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
                    
        return result