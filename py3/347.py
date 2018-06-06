class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_t = dict()
        rst = list()

        for num in nums:
            if hash_t.get(num):
                hash_t[num] += 1
            else:
                hash_t[num] = 1
        
        # TODO: Implement heap sort manually

        import operator
        max_heap = sorted(hash_t.items(), key=operator.itemgetter(1), reverse=True)
        print(max_heap)
        for i in range(k):
            rst.append(max_heap[i][0])
        
        return rst
        
